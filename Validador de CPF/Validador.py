import sys

def quant_num(cpf):
    if len(cpf) == 11:
        return cpf
    else:
        # Se não tiver 11 dígitos, imprime o erro
        print("❌ ERRO: Por favor digite 11 dígitos.")
        sys.exit()


def somente_numeros(cpf):
  cpfsemponto = cpf.replace('.', '')
  cpfsemtrco = cpfsemponto.replace('-', '')
  if cpfsemtrco.isdigit():
    return cpfsemtrco
  else:
    return None