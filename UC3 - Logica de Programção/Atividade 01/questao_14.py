# Atividade: A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado..
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024

km_percorridos = float(input('Insira a quantidade de Km percorrida pelo usuário do veículo: '))
dias_alugado = int(input('Insira a quantidade de dias em que foi alugado: '))

# Magimatica
km_total_valor = 0.20 * km_percorridos
dias_total_valor = dias_alugado * 90

#Resposta do programa com formatação dos decimais
print('\nO total do aluguel do carro foi de: R${:.2f}'.format(km_total_valor + dias_total_valor))
print('\nValor de uso pela kilometragem foi de: R${:.2f}'.format(km_total_valor), '\nValor de uso pela quantidade de', dias_alugado,'dias teve o valor de', dias_total_valor)