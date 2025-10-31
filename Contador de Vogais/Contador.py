def contador_vogais(frase): 
    vogais = 'aeiouáéíóúàèìòùãõ'

    quantidade_vogais = len([caractere for caractere in frase.lower() if caractere in vogais])

    return quantidade_vogais

def somente_digitos(frase):
    numeros = '1234567890'
    
    for caractere in frase:
        if caractere in numeros:
            
            return True
        return False
    
