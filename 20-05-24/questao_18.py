# Atividade: O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no
# peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o
# indivíduo dentro de certas faixas.
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - Entre 25 e 30: Sobrepeso
# - Entre 30 e 40: Obesidade
# - Acima de 40: Obesidade mórbida
# Obs.: O IMC é calculado pela expressão peso/altura2 (peso dividido pelo quadrado da altura)
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
    altura = input("Qual é sua altura cm: ")
    if e_numero(altura):
        altura = float(altura)
        while True:
            peso = input("Agora insira seu peso: ")
            if e_numero(peso):
                peso = int(peso)
                try:
                    # Matemática
                    imc = peso / (altura * altura) * 10000
                    if imc < 18.5:
                        print(f"O seu IMC é abaixo do peso com um valor de {imc:.2f} e está abaixo de 18.5 é crítico.")
                    elif 18.5 <= imc < 25:
                        print(f"O seu IMC é um peso ideal com um valor de {imc:.2f} e está acima de 18.5 porém abaixo de 25. ")
                    elif 25 <= imc < 30:
                        print(f"O seu IMC é de sobrepeso com um valor de {imc:.2f} e está entre 25 e abaixo de 30.")
                    elif 30 <= imc <= 40: 
                        print(f"O seu IMC é de obesidade com um valor de {imc:.2f} e está entre 30 e abaixo de 40.")
                    elif imc > 40:
                        print(f"O seu IMC é de obesidade mórbida com um valor de {imc:.2f} acima de 40.")
                    break  # Saia do loop interno após inserir o peso corretamente
                except:
                    print("ALERTA! Erro desconhecido!")
            # Caso o input do usuário não seja números:
            else:
                print("ALERTA! Insira um valor com números para o seu peso. Tente novamente!")
        break  # Saia do loop externo após inserir a altura corretamente
    # Caso o input do usuário não seja números:
    else:
        print("ALERTA! Insira um valor com números para a altura. Tente novamente!")
