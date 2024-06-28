# Atividade: Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2m².
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024

altura = float(input('Insira a altura da parede: '))
largura = float(input('Imsira a largura da parede: '))

#Magimatica
area = largura * altura
tinta = area / 2
#Resposta do programa
print('Área a ser pintada: ', area, 'm²')
print('Quantidade de tinta nescessaria: ', tinta, 'litros')