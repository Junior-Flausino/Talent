def calculadora():
  while True:
    print("Calculadora")
    print("1: Soma")
    print("2: Subtracao")
    print("3: Multiplicacao")
    print("4: Divisao")
    print("0: Sair")

    opcao = input("Digite o numero para a operacao desejada: ")

    if opcao == "0"
      print("Saindo da calculadora.")
      break
    elif opcao in ["1", "2", "3", "4"]:
      valor1 = float(input("Digite o primeiro valor: "))
      valor2 = float(input("Digite o segundo valor: "))

     if opcao == '1':
                resultado = valor1 + valor2
                print("Resultado:", resultado)
            elif opcao == '2':
                resultado = valor1 - valor2
                print("Resultado:", resultado)
            elif opcao == '3':
                resultado = valor1 * valor2
                print("Resultado:", resultado)
            elif opcao == '4':
                if valor2 != 0:
                    resultado = valor1 / valor2
                    print("Resultado:", resultado)
                else:
                    print("Não é possível dividir por zero.")
        else:
            print("Essa opção não existe.")

            print()

  calculadora()