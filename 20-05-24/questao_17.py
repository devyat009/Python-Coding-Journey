# Atividade: Escreva um programa para aprovar ou não o empréstimo bancário para a
# compra de uma casa. O programa vai perguntar o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal,
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
# Data: 22/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Função para checar se o input do usuário é número:
def e_numero(string):
    try:
        if string.isnumeric():
            string = int(string)
            return True   
        else:
            string = float(string)
            return True # Colocamos False para termos apenas valores inteiros
    except ValueError:
        return False

# Programa em loop para validar o input:
while True:
    salario = input("Insira o valor de seu salário: ")
    if e_numero(salario):
        salario = float(salario)
        while True:
            casa = input("Insira o valor da residência: ")
            if e_numero(casa):
                casa = float(casa)
                while True:
                    anos = input("Insira a quantidade de anos que deseja parcelar: ")
                    if e_numero(anos):
                        anos = int(anos)
                        prestacao_limite = salario * 30/100
                        meses = anos * 12
                        parcelas = casa / meses
                        # Caso seja possivel aprovar o empréstimo:
                        if parcelas <= prestacao_limite:
                            print(f"Empréstimo aprovado, as parcelas sairam no valor de R${parcelas:.2f}")
                        # Caso não seja possivel apaprovar o empréstimo:
                        else:
                            print(f"O empréstimo não foi aprovado, pois as parcelas ultrapassaram os 30%, ficando em {parcelas:.2f}")
                    # Caso o input do usuário não seja números:
                    else:
                        print("ALERTA! Insira um valor com números para a altura. Tente novamente!")
                break
            # Caso o input do usuário não seja números:
            else:
                print("ALERTA! Insira um valor com números para a residência. Tente novamente!")
        break
    # Caso o input do usuário não seja números:
    else:
        print("ALERTA! Insira um valor com números para o salário. Tente novamente!")