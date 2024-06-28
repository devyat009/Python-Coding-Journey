# Atividade:  Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024

dias = int(input('Insira o quantidade dias trabalhados no mês: '))

# Magimatica

horas_trabalhadas = dias * 8
salario = horas_trabalhadas * 25

print('O salário foi de R$', salario, ', tendo um total de', horas_trabalhadas,'horas trabalhadas')