# Atividade:
# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade. 
# 2 - Utilizando o dicionário criado no item 1:  
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa); 
# Adicione um campo de profissão para essa pessoa; 
# Remova um item do dicionário. 
# 3 - Crie um dicionário para representar números e seus quadrados de 1 a 5. 
# 4 - Crie um dicionário que verifique se uma chave específica existe dentro desse dicionário. 
# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
#
# Instrutor: Brunno
# Data: 04/06/2024
# Ultima Edição: 06/06/2024
# Autor: Higor Stanley aka Devyat009
# Programa: Dicionários

# IDEIA DESCARTADA
# def adicionar_pessoas(pessoas):
    # nome = input('▶ Digite o nome: ')
    # idade = input('▶ Digite qual é a idade da pessoa: ')
    # profissao = str(input('▶ Qual é a profissão dessa pessoa: '))
    # print(f'Pessoa 1: Nome - {nome[0]} Idade - {idade} Profissão - {profissao}')

# ⫷⫷⫷⫷⫷⫷⫷⫷ FUNÇÕES ⫸⫸⫸⫸⫸⫸⫸⫸⫸
# Função para checar se o input do usuário é número:
def e_numero(string):
    try:
        if string.isnumeric():
            string = int(string)
            return True   
        else:
            string = float(string)
            return False # Colocamos False para termos apenas valores inteiros
    except ValueError:
        return False
    
# Função para checar se o input do usuário é uma string:
def e_letra(string):
    try:
        if string.isalpha():
            string = str
            return True
        else:
            return False
    except ValueError:
        return False


#### QUESTÃO 2
dados_pessoais = [
        {'nome': 'Higor', 'idade': '22', 'profissao': ' ', 'cidade': 'sobradisley'},
        {'nome': 'Luiz', 'idade': '21', 'profissao': ' ', 'cidade': 'sobradisley'}
    ]

# Pessoas fixas
def pessoas():
    # Verifica se existem pessoas na lista:
    if not dados_pessoais:
        print('◇ A lista está vazia!')
        return
    # Caso contenha, imprime o seguinte:
    
    print('◇ A lista contem as seguintes pessoas: ')
    for i, pessoa in enumerate(dados_pessoais, start=1):
        print(f'◇ Pessoa {i}: Nome: {pessoa["nome"]}, Idade: {pessoa["idade"]}, Profissão: {pessoa["profissao"]}')

# Alterar a idade da lista dicionário:
def alterar_idade_pessoas(dados_pessoais):
    print('◇ Escolha a pessoa que deseja alterar: ')
    pessoas()
    # Escolhe o alvo:
    alvo = int(input('▶ Escolha o numero da pessoa que deseja alterar: '))
    nova_idade = int(input(f'▶ Insira a nova idade de {dados_pessoais[alvo - 1]["nome"]}: '))
    dados_pessoais[alvo -1]['idade'] = nova_idade
    print(f'◇ A nova idade de {dados_pessoais[alvo - 1]["nome"]} é {dados_pessoais[alvo -1]["idade"]}') 

# Adiciona uma profissão na lista dicionário:
def adicionar_profissao_pessoas(dados_pessoais):
    print('◇ Escolha a pessoa que deseja alterar: ')
    pessoas()
    # Alvo
    alvo = int(input('▶ Escolha o numero da pessoa que deseja alterar: '))
    nova_profissao = input(f'▶ Insira a nova profissão de {dados_pessoais[alvo - 1]["nome"]}: ')
    dados_pessoais[alvo -1]['profissao'] = nova_profissao
    print(f'◇ A nova profissão de {dados_pessoais[alvo - 1]["nome"]} é {dados_pessoais[alvo -1]["profissao"]}') 

# Deletar as pessoas na lista dicionário:
def deletar_pessoas():
    print('◇ Escolha a pessoa que deseja alterar: ')
    pessoas()
    # Caso tenha, tentar:
    try:
        # Usuario escolhe o estabelecimento alvo da lista:
        alvo = int(input('▶ Digite o número da pessoa em que deseja remover: '))
        # Se numero alvo do estabelecimento for menor que 0
        if 0 < alvo <= len(dados_pessoais):
            print('◇ Você confirma sua escolha? LEMBRE-SE NÃO É POSSÍVEL REVERTER (s/n)')
            escolha = input('▶ Escolha: ').lower()
            if escolha == 's':
                # Usamos rest_alvo - 1 pois o for começa do 0
                pessoa_removida = dados_pessoais.pop(alvo - 1)
                print(f'◇ A pessoa {pessoa_removida["nome"]} foi removido com SUCESSO! ✓')
            elif escolha == 'n':
                print('◇ Cancelando...')
            else:
                print('⚠︎ Insira um valor valido!')
    except ValueError:
        print('⚠︎ Insira um valor valido!')

# Sub Menu para opção PESSOAS
def sub_menu_pessoas():
    while True:
        print('┏━╾──────────────────────────────────╼━┓')
        print('┃〔 1  ☰  Listar pessoas           〕  ┃')
        print('┃〔 2  ✎  Alterar a idade          〕  ┃')
        print('┃〔 3  ✎  Adiconar a profissão     〕  ┃')
        print('┃〔 4  ✗  Deletar uma pessoa       〕  ┃')
        print('┃〔 5  ⇦  Voltar ao menu principal 〕  ┃')
        print('┗━╾──────────────────────────────────╼━┛')
        
        escolha = input('▶ Sua escolha é: ')
        if e_numero(escolha):
            escolha = int(escolha)
            match escolha:
                case 1:
                    pessoas()
                case 2:
                    alterar_idade_pessoas(dados_pessoais)
                case 3:
                    adicionar_profissao_pessoas(dados_pessoais)
                case 4:
                    deletar_pessoas()
                case 5:
                    # Sair do loop e voltar ao menu principal
                    break
                case _:
                    print('⚠︎ Alerta! Insira um número valido de 1 a 5 e tente novamente!')
        else:
            print('⚠︎ Insira um número correspondente a uma opção válida!')

#### QUESTAO 3

# Escolher número:
def alterar_numero():
        x = input('▶ Escolha um número para saber o quadrado: ')
        while True:
            if e_numero(x): 
                x = int(x)
                for i in range(1, x+1):
                    print(f'◇ O quadrado de {i} é: {i**2}')
                numeros = {x:x**2 for x in range(1,x+1)}
                print(f'◇ Resultando um dicionario: {numeros}')
                return numeros
                #break
            else:
                print('⚠︎ Insira um número correspondente a uma opção válida!')

# Menu dos Números:
def numeros_quadrado():
    
    numeros_ao_quadrado = []
    numeros_ao_quadrado.append(alterar_numero())
    while True:
        print('┏━╾──────────────────────────────────╼━┓')
        print('┃〔 1  ☰  Listar dicíonario          〕┃')
        print('┃〔 2  ✎  Alterar o número           〕┃')
        print('┃〔 3  ⇦  Voltar ao menu principal   〕┃')
        print('┗━╾──────────────────────────────────╼━┛')
        
        escolha = input('▶ Sua escolha é: ')
        if e_numero(escolha):
            escolha = int(escolha)
            match escolha:
                case 1:
                    print(numeros_ao_quadrado)
                case 2:
                    alterar_numero()
                case 3:
                    # Sair do loop e voltar ao menu principal
                    break
                case _:
                    print('⚠︎ Alerta! Insira um número valido de 1 a 3 e tente novamente!')
        else:
            print('⚠︎ Insira um número correspondente a uma opção válida!')

#### QUESTÃO 4
# Adicona um dicionario  a partir de uma frase sem regras para a questão 4 e 5:
lista_dicionario = []

# Adiconar varias frases para o dicionario:
def adicionar_dicionario():
    dicionario = {}
    while True:
        frase_customizada = input('▶ Escreva a frase para adicionar ao dicionario: ').lower()
        dicionario[frase_customizada] = dicionario.get(frase_customizada, 0) + 1
        lista_dicionario.append(dicionario)  # Adiciona o novo dicionário à lista
        continuar = input("◇ Deseja adicionar mais frases? (s/n): ").lower()
        if continuar != 's':
            return dicionario
            
# Verificar se a palavra exite e quantas vezes apareceu:        
def verificar_palavra(dicionario):
    # Identifica se o dicionário está vazio:
    if not dicionario:
        print('⚠︎ O dicionário está vazio.')
        return
    
    # Identifica o input do usuário:
    while True:
        chave = input('▶ Escolha uma palavra chave: ').strip().lower()  # Remove espaços em branco e converte para minúsculas
        if e_letra(chave):
            #chave = str(chave) # LINHA 
            # Verifica quantas vezes foi encontrada no dicionário:
            if chave in dicionario:
                print(f'◇ A palavra chave "{chave}" foi encontrada {dicionario[chave]} vezes.')
                break
            else:
                print('⚠︎ Palavra chave não encontrada!')
                break
        else:
            print('⚠︎ Insira uma palavra válida!')




# Listar o dicionario:          
def listar_dicionario(dicionario):
    print('◇ A lista do dicionario contem: ')
    for i, (frase, frequencia) in enumerate(dicionario.items(), start=1):
        print(f'◇ Frase {i}: {frase} - Frequência da frase: {frequencia}')
#### QUESTÃO 5
# Contar a frequência:
def contar_frequencia(dicionario):
    frequencia_palavras = {}
    # Iterar sobre cada frase no dicionário:
    for frase, freq in dicionario.items():
        # Dividir a frase em palavras:
        palavras = frase.split()
        # Iterar sobre cada palavra na frase:
        for palavra in palavras:
            palavra = palavra.lower()  # Convertendo a palavra para minúsculas
            if palavra in frequencia_palavras:
                # Se a palavra já estiver no dicionário de frequência, incrementar sua contagem
                frequencia_palavras[palavra] += freq
            else:
                # Se a palavra não estiver no dicionário de frequência, adicioná-la com a frequência correspondente
                frequencia_palavras[palavra] = freq
    return frequencia_palavras
    
        
    
# Sub Menu Questão 4 e 5 - Dicionário:
def menu_dicionario():
    while True:
        print('┏━╾──────────────────────────────────╼━┓')
        print('┃〔 1  ＋Dicionário                 〕 ┃')
        print('┃〔 2  ⌨ Verificar palavra          〕 ┃')
        print('┃〔 3  ☲ Contar frequência          〕 ┃')
        print('┃〔 4  ☲ Listar dicionário          〕 ┃')
        print('┃〔 5  ⇦  Voltar ao menu principal  〕 ┃')
        print('┗━╾──────────────────────────────────╼━┛')

        escolha = input('▶ Sua escolha é: ')
        if e_numero(escolha):
            escolha = int(escolha)
            match escolha:
                case 1:
                    dicionario = adicionar_dicionario()
                case 2:
                    verificar_palavra(dicionario)
                case 3:
                    frequencia = contar_frequencia(dicionario)
                    print(frequencia)
                case 4:
                    listar_dicionario(dicionario)
                case 5:
                    # Sair do loop e voltar ao menu principal
                    break
                case _:
                    print('⚠︎ Alerta! Insira um número valido de 1 a 5 e tente novamente!')
        else:
            print('⚠︎ Insira um número correspondente a uma opção válida!')

# Menu Principal
def menu():
    print('┏━╾──────────────────────────────────╼━┓')
    print('┃〔 1  ＋Pessoas                 〕    ┃')
    print('┃〔 2  ☰ Números                 〕    ┃')
    print('┃〔 3  ☲ Dicionário              〕    ┃')
    print('┃〔 4  ⤾ Sair do aplicativo      〕    ┃')
    print('┗━╾──────────────────────────────────╼━┛')

# Launcher do Programa
def main():
    while True:
        menu()
        escolha_opcao = input('▶ Sua escolha é: ')
        if e_numero(escolha_opcao):
            escolha_opcao = int(escolha_opcao)
            match escolha_opcao:
                case 1:
                    sub_menu_pessoas()
                case 2:
                    numeros_quadrado()
                case 3:
                    menu_dicionario()
                case 4:
                    print('◇ Saindo.....')
                    return  # Sair da função main e terminar o programa:
                case _:
                    print('⚠︎ Alerta! Insira um número valido de 1 a 4 e tente novamente!')
        else:
            print('⚠︎ Alerta! Insira um número valido de 1 a 4 e tente novamente!')

# Inicar o programa:
main()