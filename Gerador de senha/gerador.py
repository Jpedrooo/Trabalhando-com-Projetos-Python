import random
import string

def verificar(palavra):
    palavra = palavra.lower()
    if palavra == "gerar":
        return True
    else:
        return False
    
def gerador(comprimento):
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha