# Atividade: Crie um programa que leia o tamanho de três segmentos de reta.
# Analise seus comprimentos e diga se é possível formar um triângulo com essas retas.
# Matematicamente, para três segmentos formarem um triângulo,
# o comprimento de cada lado deve ser menor que a soma dos outros dois
# Data: 20/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# ERRO NA DEF
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
    
while True:
    a, b, c = input("Insira o seguimentos da reta serapados por ',': ").split(',')

    if e_numero(a):
        a = float(a)
        while True:
            if e_numero(b):
                b = float(b)
                while True:
                    if e_numero(c):
                        c = float(c)
                        if a < b + c or b < a + c or c < b + a:
                            print("E possivel fazer um triangulo com os valores fornecidos")
                            break
                        else:
                            print("NAO e possivel fazer um triangulo comos valores fornecidos")
                            break
                    else:
                        print("Insira um valor numerico para C")
                break
            else:
                print("Insira um valor numerico para B")
        break
    else:
        print("Insira um valor numerico para A")