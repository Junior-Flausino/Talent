def calculadora(num1, num2, operacao):
  if operacao == 1:
    resultado = num1 + num2
  elif operacao == 2:
    resultado = num1 - num2
  elif operacao == 3:
    resultado = num1 * num2
  elif operacao == 4:
    if num != 0:
      resultado = num1 / num2
      else:
        print("Nao e possivel dividir por zero.")
        return None

  else:
    print("Operacao invalida")
    return 0

    return resultado