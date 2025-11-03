import contadores
frase = input("Digite um texto: ")

lista_de_frases = frase.split()

contador =  contadores.contador_de_letras(lista_de_frases)
verificando = contadores.verificador(contador)

print(f"as palavras com mais de 10 digitos são: {contador}")

