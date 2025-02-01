from tkinter import *
from PIL import Image, ImageTk
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

#frames

frame_l = Frame(tela, width= 400, height= 400, bg=cor_secundaria)
frame_l.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_2= Frame(tela, width=300, height=500, bg=cor_principal)
frame_2.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_3=Frame(tela, width=800, height=100, bg=cor_terciaria)
frame_3.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

#parte da logo
logo = Image.open('AUDIORA/img/musicicon.png')
logo = ImageTk.PhotoImage(logo)

l_imagem = Label(frame_l, height= 300, image=logo, compound= LEFT, padx=10, anchor='nw', font=('ivy 16'), bg=cor_secundaria)
l_imagem.place(x=60,y=20)

#parte das musicas
musicas= ['text','text','text']
listbox = Listbox(frame_2, selectmode=SINGLE, width=60, height=32, font=(fonte, 9),bg=cor_principal, fg=cor_secundaria)
listbox.grid(row=0, column=0)

s= Scrollbar(frame_2)
s.grid(row=0,column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

for i in musicas:
    listbox.insert(END,i)

#criando o rodape de musica
i_voltar = Image.open('AUDIORA/img/botao_voltar.png')

i_voltar = ImageTk.PhotoImage(i_voltar)

l_rodando = Label(frame_l, text= 'Escolha música na lista', width= 20, justify=CENTER, anchor='nw', font=(fonte), bg=cor_secundaria)
l_rodando.place(x=125,y=350)

#botao de voltar

b_voltar = Button(frame_l, width= 35, height=14, image=i_voltar, font=(fonte),relief=FLAT, overrelief=RIDGE, bg=cor_secundaria)
b_voltar.place(x=100,y=390)

#botao de play
i_play = Image.open('AUDIORA/img/botao_play.png')

i_play = ImageTk.PhotoImage(i_play)

b_play= Button(frame_l, width= 35, height=25, image=i_play, font=(fonte),relief=FLAT, overrelief=RIDGE, bg=cor_secundaria)
b_play.place(x=190,y=380)

#botao de avançar
i_avancar = Image.open('AUDIORA/img/botao_avançar.png')

i_avancar = ImageTk.PhotoImage(i_avancar)

b_avancar= Button(frame_l, width= 35, height=15, image=i_avancar, font=(fonte),relief=FLAT, overrelief=RIDGE, bg=cor_secundaria)
b_avancar.place(x=250,y=390)




tela.mainloop()



