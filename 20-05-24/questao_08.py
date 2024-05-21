# Atividade: Faça um algoritmo que pergunte a distância que um passageiro deseja
# percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
# viagens até 200Km e R$0.45 para viagens mais longas.
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Função para checar se o input do usuário e número:
def e_numero(string):
    try:
        if string.isnumeric():
            string = int(string)
            return True
        else:
            string = float(string)
            return True
    except ValueError:
        return False

# Programa em loop para validar o input:
while True:
    km = input("Insira a quantidade de KM em que deseja percorer: ")
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(km):
        km = float(km)
        # Caso a quilometragem seja igual o menor que 200:
        if km <= 200:
            print(f"O preco da passagem sera de: R${km*0.50}")
            break
        # Caso a quilometragem seja maior que 200 aplicar outra tarifa:
        elif km > 200:
            print(f"O preco da passagem sera de: R${km*0.45}")
            break
    # Caso o input não seja numérico:
    else:
        print("ALERTA! Insira um valor com números. Tente novamente!")