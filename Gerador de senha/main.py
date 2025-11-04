import random
import string
import gerador

gerar = input("Gigite a palavra gerar, para gerar uma senha :")
correto = gerador.verificar(gerar)
try:
    if correto == True:
        senha = gerador.gerador(12)
        print("Senha gerada:", senha)
    
except Exception as e:
    print(f"Ocorreu um erro:")
    print("senha não gerada")