import sys

lista = []

def verificador(resposta):
    numeros = ["1", "2", "3", "4"]
    if not resposta.isdigit():
        print("Digite apenas numeros")
        sys.exit()
    if resposta not in numeros:
        print("Opção inválida. Digite um número de 1 a 4.")
        sys.exit()
    return True

while True:
    
    resposta = input("""
1. Adicionar tarefa
2. Visualizar tarefas
3. Remover tarefa
4. Sair
Escolha uma opção: """)

    if not verificador(resposta):
        continue
    
    if resposta == "1":
        adicionando = input("digite a tarefa: ")
        lista.append(adicionando)
        print("Tarefa adicionadaa")
        
    elif resposta == "2":
        print(f""" Tarefas:
{lista}""")
        
    elif resposta == "3":
        try:
            removida = input("Digite o número da tarefa a ser removida: ")
            numero_tarefa = int(removida)
        
            indice_remover = numero_tarefa - 1
        
            if numero_tarefa < 1 or numero_tarefa > len(lista):
                print("❌ Erro: Número de tarefa inválido ou inexistente.")
            else:
                removendo = lista.pop(indice_remover)
                print(f"item {removendo} removido")
        except ValueError:
            print("❌ Erro: Por favor, digite um número válido.")
        
    elif resposta == "4":
        sys.exit()
    
        
    
    
    