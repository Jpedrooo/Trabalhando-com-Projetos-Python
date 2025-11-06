def sacar_dinheiro():
    
    CEDULAS = [100, 50, 20, 10, 5, 2]
    
    valor_saque = 0

    
    while True:
        entrada = input("💳 Digite o valor do saque (Múltiplo de R$ 2,00): R$ ")
        
        try:
            valor_saque = int(entrada)

            if valor_saque <= 0:
                print("❌ Erro: O valor do saque deve ser positivo.")
            
            
            elif valor_saque % 2 != 0:
                print("❌ Erro: Não há cédulas de R$ 1,00. O valor deve ser múltiplo de R$ 2,00.")
            
            else:
                
                break 

        except ValueError:
            print("❌ Erro: Por favor, digite um valor numérico inteiro válido.")

    
    
    contagem_cedulas = {}
    valor_restante = valor_saque

    print(f"\nCaixa Eletrônico: Entregando R$ {valor_saque},00")
    print("--- Detalhes do Saque ---")

    
    for cedula in CEDULAS:
        
        quantidade = valor_restante // cedula 
        
        if quantidade > 0:
            
            contagem_cedulas[f"R$ {cedula},00"] = quantidade
            
            
            valor_restante = valor_restante % cedula
            
            print(f"| {quantidade} x Cédulas de R$ {cedula},00")
    
    print("-------------------------")
    print("✅ Saque concluído.")
    
    
    if valor_restante != 0:
        print(f"⚠️ Alerta: Sobrou um valor de R$ {valor_restante},00 que não pôde ser entregue.")



sacar_dinheiro()