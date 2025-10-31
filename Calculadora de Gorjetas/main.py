import calculadora

Valor_conta = input("Digite o valor da conta: ")
Porcentagem_gorj = input("Digite a porcentagem da gorjeta: ")

conta_limpa, porcentagem_limpa = calculadora.verificacao(Valor_conta, Porcentagem_gorj)

resultado_gojeta = calculadora.calculadora_gorjeta(conta_limpa, porcentagem_limpa)
resultado_total = calculadora.valor_tot(resultado_gojeta, conta_limpa)
print(f"Valor da gorjeta: {resultado_gojeta}")
print(f"valor total da conta: {resultado_total}")