# Atividade: Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e  
# mostre na tela: 
# a) Quais foram os números sorteados 
# b) Quantos números estão acima de 5 
# c) Quantos números são divisíveis por 3 
# Data: 27/05/2024
# Instrutor: Brunno
# Autor: Higor Stanley

# Importa random para sortear os números:
import random;

# Listas
sorteados = []
divisivel = []
acimaCinco = []

# Sorteio do programa
for i in range(20):
    numero_sorteado = random.randint(0, 10)
    sorteados.append(numero_sorteado)
    if numero_sorteado >= 5:
        acimaCinco.append(numero_sorteado)
    elif numero_sorteado % 3 == 0:
        divisivel.append(numero_sorteado)
# Resposta do programa:
print(f'Os números que são acima de cinco: {acimaCinco}', end=' ')
print(f'\nOs números que são divisíveis: {divisivel}', end=' ')

    
        
    
    
    