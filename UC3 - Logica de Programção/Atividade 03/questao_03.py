# Atividade:  Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1,  
# marcando os números que forem divisíveis por 4, exatamente como mostrado abaixo: 
# 30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]... 
# Data: 24/05/2024
# Ultima edição: 27/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Input do usuário:
numero = int(input('Insira um número: '))

# Para realizar a contagem regressiva colocamos '-1,-1'
for i in range(numero, -1, -1):
    if i % 4 == 0:
        print(f"[{i}]", end=' ')
    else:
        print(i, end=' ')