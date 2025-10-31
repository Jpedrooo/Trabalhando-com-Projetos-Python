import Contador

frase = input("Digite um texto: ")


if not frase:
    print("Erro: Você não digitou nada. Por favor, insira um texto.")


elif Contador.somente_digitos(frase):
    
    print("Erro: Por favor, digite somente letras, e não números.")


else:
    Quantidade = Contador.contador_vogais(frase)
    
    if Quantidade == 0:
        print(f"O texto '{frase}' não tem vogais.")
    else:
        print(f"O texto tem {Quantidade} vogais.\n {frase}")