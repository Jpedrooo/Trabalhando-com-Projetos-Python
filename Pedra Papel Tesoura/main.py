import random

escolha = input("Escolha: pedra, papel ou tesoura?")
lista = ["pedra", "papel", "Tesoura"]

def escolha_doBot():
    palavra_secreta = random.choice(lista)
    return palavra_secreta

def vencedor(escolha, escolha_do_Bot):
    escolha = escolha.lower()
    escolha_do_Bot = escolha_do_Bot.lower()
    if escolha == "pedra" and escolha_do_Bot == "tesoura":
        return("VocÊ GANHOU! o bot escolheu : ", escolha_do_Bot)
    elif escolha == "tesoura" and escolha_do_Bot == "papel":
        return("VocÊ GANHOU! o bot escolheu : ", escolha_do_Bot)
    elif escolha == "papel" and escolha_do_Bot == "pedra":
        return("VocÊ GANHOU! o bot escolheu : ", escolha_do_Bot)
    elif escolha == "pedra" and escolha_do_Bot == "papel":
        return("VocÊ PERDEU! o bot escolheu : ", escolha_do_Bot)
    elif escolha == "tesoura" and escolha_do_Bot == "pedra":
        return("VocÊ PERDEU! o bot escolheu : ", escolha_do_Bot)
    elif escolha == "papel" and escolha_do_Bot == "tesoura":
        return("VocÊ PERDEU! o bot escolheu : ", escolha_do_Bot)
    elif escolha == escolha_do_Bot:
        return("empate", escolha_do_Bot)

computador = escolha_doBot()
resultado = vencedor(escolha, computador)

print(resultado)



    