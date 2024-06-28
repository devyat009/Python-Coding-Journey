# Atividade: Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
# Autor: Higor Stanley
# Instrutor: Brunno
# Data: 11/05/2024

print('Insira as notas do aluno para descobrir a média\n')

nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))
#Magimatica
media = (nota1+nota2)/2
print('\nO aluno teve a média de: {:.2f}' .format(media))