# Atividade: [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024
# Edit: 

garrel = int(input('Qual a quantidade diária de cigarros em que fuma? '))
anos = int(input('Há quantos anos completos ou por quantos anos, teve o hábito de fumar? '))

#Magimatica
total_garrel = (garrel * 365) * anos
# Multiplicamos o total de cigarros consumidos por 10min, depois dividimos por 60 para obtermos a quantidade de horas, e logo após dividimos por 24 para ter o resultado em dias.
total_dias_perdidos = ((total_garrel * 10) / 60) / 24

#Resposta do programa
print('Você consumiu aproximadamente', total_garrel, 'de cigarros nos ultimos', anos, 'anos', '\nPerdendo aproximadamente {:.2f}'.format(total_dias_perdidos), 'de dias de sua vida total.')