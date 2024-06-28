# Atividade: Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024

salario = float(input('Insira o valor do salário: '))
# Magimatica
reajuste = (salario * (15/100)) + salario
# Resposta do programa
print('O salário após o aumento de 15% é de: R${:.2f}'.format(reajuste))