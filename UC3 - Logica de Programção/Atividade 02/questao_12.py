# Atividade: Faça um programa que leia a largura e o comprimento de um terreno
# retangular, calculando e mostrando a sua área em m2. O programa também
# deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
# - Abaixo de 100m2 = TERRENO POPULAR
# - Entre 100m2 e 500m2 = TERRENO MASTER
# - Acima de 500m2 = TERRENO VIP
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
            return False # Colocamos False para termos apenas valores inteiros
    except ValueError:
        return False

# Função para dizer qual é o tipo de terreno:
def tipo(string):
    try:
        if string <= 100:
            return "TERRENO POPULAR"
        elif 100 > string < 500:
            return "TERRENO MASTER"
        elif string >= 500:
            return "TERRENO VIP"
    except ValueError:
        False

# Programa em loop para validar o input:
while True:
    largura = input("Insira a largura do lote em metros: ")
    # Usa a função 'e_numero' para validar o input do usuário:
    if e_numero(largura):
        largura = float(largura)
        while True:
            comprimento = input("Insira o comprimento em metros: ")
            # Usa a função 'e_numero' para validar o input do usuário:
            if e_numero(comprimento):
                comprimento = float(comprimento)
                m2 = largura * comprimento
                # Caso o terreno seja menor ou igual a 100m², portando será do tipo popular:
                if m2 <= 100:
                    # Usa a função 'tipo' para verificar e dizer qual é o tipo de terreno:
                    t = tipo(m2)
                    print(f"O terreno tem {m2}m² portando ele é do tipo: {t}")
                    break
                # Caso o terreno seja maior que 100m² e menor que 500m², portando será do tipo master:
                elif 100 > m2 < 500:
                    # Usa a função 'tipo' para verificar e dizer qual é o tipo de terreno:
                    t = tipo(m2)
                    print(f"O terreno tem {m2}m² portando ele é do tipo: {t}")
                    break
                # Caso o terreno seja maior ou igual a 500m², portando será do tipo vip:
                elif m2 >= 500:
                    # Usa a função 'tipo' para verificar e dizer qual é o tipo de terreno:
                    t = tipo(m2)
                    print(f"O terreno tem {m2}m² portando ele é do tipo: {t}")
                    break
            # Caso o input não seja numérico:
            else:
                print("ALERTA! Insira um valor valido que seja numérico para a COMPRIMENTO. Tente novamente!")
        break
    # Caso o input não seja numérico:
    else:
        print("ALERTA! Insira um valor valido que seja numérico para a LARGURA. Tente novamente!")