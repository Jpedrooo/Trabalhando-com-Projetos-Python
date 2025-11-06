try:
    x = int(input("Digite o primeiro número: "))
    operador = input("Escolha a operação (+, -, *, /): ")
    y = int(input("Digite o segundo número: "))

    def calculadora(x, y, operador):
        if operador == "+":
            resultado = x + y
        elif operador == "-":
            resultado = x - y
        elif operador == "*":
            resultado = x * y
        elif operador == "/":
            resultado = x / y
        else:
            resultado = "Opção inválida"
        return resultado

    resultado = calculadora(x, y, operador)
    print(resultado)
except ValueError:
    print(f"Entrada inválida: Digite apenas números.")
except ZeroDivisionError:
    print(f"Divisão por 0")
