# Atividade: Faça um algoritmo que pergunte ao usuário um número inteiro e positivo  
# qualquer e mostre uma contagem até esse valor: 
# Dica: usar o parâmetro end= ‘ ’ para deixar todas os prints na mesma linha 
# Ex: Digite um valor: 35 
# Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou! 
# Data: 24/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

numero = int(input('Insira um número positivo: '))

for i in range(0, numero+1):
    print(i, end= '')

print("\nAcabou!")