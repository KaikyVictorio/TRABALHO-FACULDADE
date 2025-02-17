from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer
import os
import webbrowser
import ctypes
import threading

os.chdir(r'AUDIORA/musica')
playlist = os.listdir()


cor_principal = '#000000' #preto
cor_secundaria = '#40E0D0' #turquesa
cor_terciaria = '#FFFFFF' #branco
fonte= './fonte/Poppins-Black.ttf'

#tela

tela = Tk ()
tela.title('Audiora')
tela.geometry('800x600')
tela.configure(background=cor_principal)
tela.resizable(width=FALSE, height= FALSE)

#funcoes

def play_musica():
    cantando = listbox.get(ACTIVE)
    l_rodando['text'] = cantando
    print(cantando)
    if len(cantando)>=50:
        l_rodando.place_forget()
        l_rodando.place(x=10,y=350)

    mixer.music.load(cantando)
    mixer.music.play()

def pausar_musica():
    mixer.music.pause()

def prox_musica():
    tocando = l_rodando['text']
    index = playlist.index(tocando)
    novo_index= index+1

    tocando = playlist[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()
    listbox.delete(0,END)

    lista_musicas()
    listbox.select_set(novo_index)
    listbox.configure(selectmode=SINGLE)
    l_rodando['text'] = tocando

def voltar_musica():
    tocando = l_rodando['text']
    index = playlist.index(tocando)
    novo_index= index-1

    tocando = playlist[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()
    listbox.delete(0,END)

    lista_musicas()
    listbox.select_set(novo_index)
    listbox.configure(selectmode=SINGLE)
    l_rodando['text'] = tocando

def dowload():
    webbrowser.open('https://mp3converter.fr/pt/youtube-para-mp3/')

def get_volume():
    devices =ctypes.windll.winmm.waveOutGetVolume
    volume = ctypes.c_uint()
    devices(0, ctypes.byref(volume))
    return (volume.value & 0xFFFF) / 0xFFFF * 100

def por_volume(val):
    volume = int(float(val) / 100 * 0xFFFF)
    vol = volume | (volume << 16)
    ctypes.windll.winmm.waveOutSetVolume(0, vol)

def mudar_volume():
        current_volume = get_volume()
        bar_volume.set(current_volume)
        tela.after(1000, mudar_volume)  
#frames

frame_l = Frame(tela, width= 400, height= 400, bg=cor_secundaria)
frame_l.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_2= Frame(tela, width=300, height=500, bg=cor_principal)
frame_2.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_3=Frame(tela, width=800, height=100, bg=cor_terciaria)
frame_3.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

#parte da logo
logo = Image.open('C:/Users/Kaiky Victório/Documents/faculdade/AUDIORA/img/musicicon.png')
logo = ImageTk.PhotoImage(logo)

l_imagem = Label(frame_l, height= 300, image=logo, compound= LEFT, padx=10, anchor='nw', font=('ivy 16'), bg=cor_secundaria)
l_imagem.place(x=60,y=20)

#parte das musicas
listbox = Listbox(frame_2, selectmode=SINGLE, width=60, height=32, font=(fonte, 9),bg=cor_principal, fg=cor_secundaria)
listbox.grid(row=0, column=0)

#barra de scrollar
s= Scrollbar(frame_2)
s.grid(row=0,column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)


#criando o rodape de musica
i_voltar = Image.open('C:/Users/Kaiky Victório/Documents/faculdade/AUDIORA/img/botao_voltar.png')

i_voltar = ImageTk.PhotoImage(i_voltar)

l_rodando = Label(frame_l, text='Selecione uma música!' , width= 60, justify=CENTER, anchor='nw', font=(fonte), bg=cor_secundaria)
l_rodando.place(x=125,y=350)

#botao de voltar

b_voltar = Button(frame_l, command=voltar_musica, width= 35, height=14, image=i_voltar, font=(fonte),relief=FLAT, overrelief=RIDGE, bg=cor_secundaria)
b_voltar.place(x=140,y=386)

#botao de play
i_play = Image.open('C:/Users/Kaiky Victório/Documents/faculdade/AUDIORA/img/botao_play.png')

i_play = ImageTk.PhotoImage(i_play)

b_play= Button(frame_l,command=play_musica, width= 35, height=25, image=i_play, font=(fonte),relief=FLAT, overrelief=RIDGE, bg=cor_secundaria)
b_play.place(x=175,y=380)

#botao de pause
i_pause = Image.open('C:/Users/Kaiky Victório/Documents/faculdade/AUDIORA/img/botao_pause.png')

i_pause = ImageTk.PhotoImage(i_pause)

b_pause= Button(frame_l, command=pausar_musica, width= 35, height=25, image=i_pause, font=(fonte),relief=FLAT, overrelief=RIDGE, bg=cor_secundaria)
b_pause.place(x=205,y=380)


#botao de avançar
i_avancar = Image.open('C:/Users/Kaiky Victório/Documents/faculdade/AUDIORA/img/botao_avançar.png')

i_avancar = ImageTk.PhotoImage(i_avancar)

b_avancar= Button(frame_l, command=prox_musica, width= 35, height=15, image=i_avancar, font=(fonte),relief=FLAT, overrelief=RIDGE, bg=cor_secundaria)
b_avancar.place(x=245,y=386)

#botao de dowload
i_dowload= Image.open('C:/Users/Kaiky Victório/Documents/faculdade/AUDIORA/img/botao_dowload.png')
i_dowload= ImageTk.PhotoImage(i_dowload)

b_dowload= Button(frame_l, command=dowload, width= 45, height=25, image=i_dowload, font=(fonte),relief=FLAT, overrelief=RIDGE, bg=cor_secundaria)
b_dowload.place(x=360,y=450)

#barra de volume
t_volume = Label(frame_3,text= 'Volume', width= 40, justify=CENTER, anchor='nw',font= (fonte))
t_volume.place(x=00, y=200)
bar_volume = ttk.Scale(frame_3, from_=0, to=100, orient="horizontal", command=por_volume)
bar_volume.pack()

def lista_musicas():
    for i in playlist:
        listbox.insert(END,i)


lista_musicas()
mixer.init()
threading.Thread(target=mudar_volume, daemon=True).start()

tela.mainloop()



