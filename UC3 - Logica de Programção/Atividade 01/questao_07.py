# Atividade: Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024

numero = float(input('Insira o valor desejado: '))
# Magimatica
dobro = numero * 2
terca = numero / 3
# Resposta do programa
print('O dobro do número:', numero, 'é de', dobro, 'e a terça parte é {:.3f}'.format(terca))