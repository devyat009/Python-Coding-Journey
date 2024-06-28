# Atividade: Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela  
# qual foi o maior e qual foi o menor preço digitado. 
# Data: 27/05/2024
# Instrutor: Brunno
# Autor: Higor Stanley

# Função para checar se o input do usuário é número:
def e_numero(string):
    try:
        if string.isnumeric():
            string = int(string)
            return True   
        else:
            string = float(string)
            return True # Colocamos False para termos apenas valores inteiros
    except ValueError:
        return False

# Lista:
produtos = []

# Loop do programa para validações:
while True:
    # Loop do programa para validações:
    # Pede as informações para o usuário:
    quantidade = input('Insira a quantidade de produtos que dejesa inserir o preço: ')
    if e_numero(quantidade):
        quantidade = int(quantidade)
        for i in range(0, quantidade):
            while True:
                produ = input(f'Insira o preço do produto {i+1}: R$ ')
                if e_numero(produ):
                    produ = float(produ)
                    produtos.append(produ)
                    produtos.sort()
                    break
                # Caso o input não seja numérico:
                else:
                    print("\nALERTA! Insira um valor com números. Tente novamente!")
        # A respota do programa:
        print(f'O menor preço foi de: R${produtos[0]}')
        print(f'O maior preço foi de: R${produtos[-1]}')
        #Sair do loop
        break
    # Caso o input não seja numérico:
    else:
        print("\nALERTA! Insira um valor com números. Tente novamente!")