import os

file_path = 'C:/Users/Kaiky Victório/Documents/faculdade/AUDIORA/musicicon.png'

# Verificar se o arquivo existe
if os.path.exists(file_path):
    print("O arquivo existe!")
else:
    print("Arquivo não encontrado!")
