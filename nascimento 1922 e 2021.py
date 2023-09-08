import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano fora do intervalo válido. Tente novamente.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    nome_completo = input("Digite o seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    
    print(f"Olá, {nome_completo}!")
    print(f"Em 2022, você completou ou completará {idade} anos.")

if __name__ == "__main__":
    main()
