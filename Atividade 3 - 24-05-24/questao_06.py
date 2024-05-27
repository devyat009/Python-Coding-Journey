# Atiivade: Crie um programa que leia 6 números inteiros e no final mostre quantos deles  
# são pares e quantos são ímpares. 
# Data: 27/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Input do usuário:
numero = int(input('Insira a quantidade de números que deseja escrever: '))
lista_par = []
lista_impar = []

for i in range(0, numero):
    insira = int(input(f'Insira o número {numero+1}:'))
    if insira % 2 == 0:
        lista_par.append(insira)
    else:
        lista_impar.append(insira)
    
# Resultado do programa:
print(f'Este são os números pares:{lista_par}')
print(f'Estes são os números ímpares:{lista_impar}')