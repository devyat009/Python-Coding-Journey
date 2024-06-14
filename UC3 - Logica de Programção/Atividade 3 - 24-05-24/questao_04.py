# Atividade: Crie um algoritmo que leia o valor inicial da contagem, o valor final e o  
# incremento, mostrando em seguida todos os valores no intervalo: 
# Ex: Digite o primeiro Valor: 3 
# Digite o último Valor: 10 
# Digite o incremento: 2 
# Contagem: 3 5 7 9 Acabou!
# Data: 27/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Pede as informações para o usuário:
primeiro = int(input('Digite o primeiro valor: '))
ultimo = int(input('Digite o ultimo valor: '))
incremento = int(input('Digite o incremento: '))

# Se for zero, cancelar toda a operação:
if incremento == 0:
    print('Infelizmente não poderemos proceguir por conta do incremento ser zero\nTente Novamente!')

else:
    # De um número postivo até o número final:
    if primeiro < ultimo and incremento > 0:
        for i in range(primeiro, ultimo +1, incremento):
            print(i, end = ' ')
    # De um número negativo até um positivo:
    elif primeiro > ultimo and incremento <  0:
        for i in range(primeiro, ultimo -1, incremento):
            print(i, end= ' ')
    # Mensagem de erro:
    else:
        print('Parece que os valores fornecidos não são válidos para esta operação')
        print('Certifique-se de que o incremento é positivo para uma contagem ascendente e negativo para uma contagem descendente')
