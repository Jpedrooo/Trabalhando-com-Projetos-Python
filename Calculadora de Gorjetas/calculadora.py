import main

def calculadora_gorjeta(conta, porcentagem):
  valor_da_gorjeta = conta * (porcentagem / 100)
  return valor_da_gorjeta

def valor_tot(gorjeta, conta):
  total = gorjeta + conta
  return total

def verificacao(conta, porcentagem):
  if not conta:
    print("O valor do da conta não foi digitado")
  elif not porcentagem:
    print("a porcentagem da comissão não foi informada")

  try:

        conta_float = float(conta.replace(',', '.'))


        porcentagem_limpa = porcentagem.replace(',', '.').replace('%', '')
        porcentagem_float = float(porcentagem_limpa)


        return conta_float, porcentagem_float
  except ValueError:
        print("❌ ERRO: Os valores digitados não são números válidos.")
        return None, None # Retorna dois Nones em caso de erro