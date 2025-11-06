import random

try:

    numero = 0
    numeroCPU = random.randint(1, 100)

    while numero != numeroCPU:
        numero = int(input("Tente adivinhar o número:(1-100) "))
    
        if numero < numeroCPU:
            print("Muito baixo! Tente um número maior.")
        elif numero > numeroCPU:
            print("Muito alto! Tente um número menor.")

    print("🎉 Parabéns! Você acertou o número!")



except ValueError:
    print("🚨 Entrada inválida! Por favor, digite APENAS números inteiros.")