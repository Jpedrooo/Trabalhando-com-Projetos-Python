import sys

def contador_de_letras(lista):
    lista_com_palavras_grandes = []

    for palavra in lista:
        if len(palavra) > 10: 
            lista_com_palavras_grandes.append(palavra)
        return lista_com_palavras_grandes
    
def verificador(lista):

    if len(lista) == 0:
        print("Não exite nenhuma palavra com mais de 10 caracteres")
        sys.exit(1)
    else:
        return lista