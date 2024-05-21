# Atividade: Faça um programa que leia a largura e o comprimento de um terreno
# retangular, calculando e mostrando a sua área em m2. O programa também
# deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
# - Abaixo de 100m2 = TERRENO POPULAR
# - Entre 100m2 e 500m2 = TERRENO MASTER
# - Acima de 500m2 = TERRENO VIP
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

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
    
while True:
    largura = input("Insira a largura do lote em metros: ")
    if e_numero(largura):
        largura = float(largura)
        while True:
            comprimento = input("Insira o comprimento em metros: ")
            if e_numero(comprimento):
                comprimento = float(comprimento)
                m2 = largura * comprimento
                if m2 <= 100:
                    t = tipo(m2)
                    print(f"O terreno tem {m2}m² portando ele é do tipo: {t}")
                    break
                elif 100 > m2 < 500:
                    t = tipo(m2)
                    print(f"O terreno tem {m2}m² portando ele é do tipo: {t}")
                    break
                elif m2 >= 500:
                    t = tipo(m2)
                    print(f"O terreno tem {m2}m² portando ele é do tipo: {t}")
                    break
            else:

                print("Insira um valor valido que seja numerico para a COMPRIMENTO")
        break
    else:
        print("Insira um valor valido que seja numerico para a LARGURA")