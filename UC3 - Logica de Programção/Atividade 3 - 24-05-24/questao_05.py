# Atividade: Crie um algoritmo que leia o valor inicial da contagem, o valor final e o  
# incremento, mostrando em seguida todos os valores no intervalo: 
# Ex: Digite o primeiro Valor: 3 
# Digite o último Valor: 10 
# Digite o incremento: 2 
# Contagem: 3 5 7 9 Acabou!
# !!!O programa acima vai ter um problema quando digitarmos o primeiro valor  
# maior que o último. Resolva esse problema com um código que funcione em qualquer situação.!!! 
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

# De um número postivo até o número final:
elif primeiro < ultimo and incremento > 0:
    for i in range(primeiro, ultimo +1, incremento):
        print(i, end = ' ')
# !!!Se o primeiro for maior que o ultimo!!!:
elif primeiro > ultimo and incremento > 0:
    # Transformar o incremento em negativo para realizar a operação, assim enganando o usuário, já que positvo adiciona,é queremos sair de um número grande para um menor:
    if incremento > 0:
        incremento = incremento * -1
        for i in range(primeiro -1, ultimo, incremento):
            print(i, end = ' ')
    else:
        print('DEBUG - Parece que você encontrou um bug que nem o programador conseguiu replicar. Favor reportar!')

# De um número negativo até um positivo:
elif primeiro > ultimo and incremento <  0:
    for i in range(primeiro, ultimo -1, incremento):
        print(i, end= ' ')

# Mensagem de erro:
else:
    print('Parece que os valores fornecidos não são válidos para esta operação')
    print('Certifique-se de que o incremento é positivo para uma contagem ascendente e negativo para uma contagem descendente')