import sys
import Validador

CPF = input("Digite o seu cpf: ")

cpf_com_onze = Validador.quant_num(CPF)
cpf_corretissimo = Validador.somente_numeros(cpf_com_onze)
if cpf_corretissimo is None:
  print("❌ ERRO: CPF inválido, contém caracteres não numéricos.")
  sys.exit(1)

print("CPF válido.")