# Atividade: Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024

print('Programa que calcula o valor de Delta (∆)')
a = int(input('Insira o valor de A: '))
b = int(input('Insita o valor de B: '))
c = int(input('Insira o valor de C: '))
#Magimatica
delta = b**2 - (4 * a * c)
#Resposta do Programa
if delta < 0 :
    print('O valor de ∆ é negativo: ', delta, '\nPortanto uma equação do segundo grau que utilize delta não haverá uma solução.')
else:
    print('O valor de ∆ é: ', delta)
