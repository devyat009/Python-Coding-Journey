# Atiivade: Crie um programa que leia 6 números inteiros e no final mostre quantos deles  
# são pares e quantos são ímpares. 
# Data: 27/05/2024
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

# Listas:
lista_par = []
lista_impar = []

# Loop do programa para validações:
while True:
    # Input do usuário:
    numero = input('Insira a quantidade de números que deseja escrever: ')
    if e_numero(numero):
        numero = int(numero)
        # Repetição para inserir os números:
        for i in range(0, numero):
            while True:
                insira = input(f'Insira o número {i+1}:')
                if e_numero(insira):
                    insira = int(insira)
                    if insira % 2 == 0:
                        lista_par.append(insira)
                        break
                    else:
                        lista_impar.append(insira)
                        break
                # Caso o input não seja numérico:
                else:
                    print("\nALERTA! Insira um valor com números. Tente novamente!")
            
        # Resultado do programa:
        print(f'Este são os números pares:{lista_par}')
        print(f'Estes são os números ímpares:{lista_impar}')
        #Sair do loop   
        break
    # Caso o input não seja numérico:
    else:
        print("\nALERTA! Insira um valor com números. Tente novamente!")