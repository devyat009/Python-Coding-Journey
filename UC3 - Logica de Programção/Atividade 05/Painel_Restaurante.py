# Atividade: 
# Descrição: 
# Crie um aplicativo de cadastro de restaurante em Python. 
# O programa precisará conter as seguintes informações: 
# ▶ Restaurante: 
# ▶ Nome 
# ▶ Categoria (Pizzaria, Japonesa, Fastfood, Churrascaria...) 
# ▶ Status (Ativado ou Desativado) 
# O programa precisará conter as seguintes informações Funções: 
# ▶ Função main() 
# ▶ Exibir nome do aplicativo 
# ▶ Exibir opções iniciais 
# ▶ Retornar ao menu principal 
# ▶ Finalizar o App 
# ▶ Opção inválida (caso seja selecionado uma opção inexistente) 
# ▶ Cadastrar o restaurante 
# ▶ Listar restaurantes 
# ▶ Alterar estado do restaurante(Ativar ou Desativar)
# Instrutor: Brunno
# Data: 03/06/2024
# Últilma Edição: 06/06/2024 
# Autor: Higor Stanley aka Devyat009
# Programa: Painel de gerenciador de estabelecimentos

# Classe Restaurante
class Restaurante:
    def __init__(self, nome, categoria, status):
        self.nome = nome
        self.categoria = categoria
        self.status = status

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

# Função para cadastrar:
def cadastrar_restaurantes(restaurantes):
    while True:
        nome = input('▶ Digite o nome do estabelecimento: ')
        categoria = input('▶ Digite qual é a categoria do estabelecimento (FastFood, Pizzaria, Restaurante): ')
        status = input('▶ Qual o status do estabelecimento, ele está ativado? (sim ou não): ').lower()
        if status == 'sim' or status == 's':
            status = True
        else:
            status = False
        restaurante = Restaurante(nome, categoria, status)
        restaurantes.append(restaurante)  # adicionamos o estabelecimento à lista
        print('◇ Cadastro realizado com SUCESSO! ✓')
        
        continuar = input("◇ Deseja adicionar mais estabelecimentos? (s/n): ").lower()
        if continuar != 's':
            break
    return restaurantes

# Lista de Restaurantes:
def listar_restaurantes(restaurantes):
    # Caso não tenha nenhum estabelecimento:
    if not restaurantes:
        print('⋄ Não tem nenhum estabelecimento cadastrado')
        return
    # Imprimimos a lista de estabelecimento cadastrados:
    print('  ESTABELECIMENTO'.ljust(20) + '▎' + '  NOME'.ljust(20) + '▎' + '  CATEGORIA'.ljust(20) + '▎' + '  STATUS'.ljust(10)) # Titulo da lista
    # Itens numerados e ajustados de acordo com o titulo:
    for i, restaurante in enumerate(restaurantes, start=1):
        nome = restaurante.nome
        categoria = restaurante.categoria
        # Convertemos o True e False para palavra
        status = "ATIVADO" if restaurante.status else "DESATIVADO" 
        print(f'Estabelecimento {i}'.ljust(20) + '▎' + f'{nome}'.ljust(20) + '▎' + f'{categoria}'.ljust(20) + '▎' + f'{status}'.ljust(10))

# Alterar o Status:
def alterar_status(restaurantes):
    # Listamos os estabelecimentos para que o usuario possa escolher oque deseja alterar o estado:
    listar_restaurantes(restaurantes)
    # Caso não tenha nenhum:
    if not restaurantes:
        return
    # Caso tenha, tentar:
    try:
        # Usuario escolhe o estabelecimento alvo da lista:
        rest_alvo = int(input('▶ Digite o número do estabelecimento em que deseja alterar o estado: '))
        # Se numero alvo do estabelecimento for menor que 0
        if 0 < rest_alvo <= len(restaurantes):
            # Usuario inseri o novo estado:
            status = input('▶ Insira o novo status, Ativado ou Desativado (sim ou não): ')
            if status == 'sim' or status == 's':
                status = True
            else:
                status = False
            # Usamos rest_alvo - 1 pois o for começa do 0
            restaurantes[rest_alvo - 1].status = status
            print(f'⋄ O estado do estabelecimento {restaurantes.nome} foi alterado com SUCESSO! ✓')
        else:
            print('⚠︎ Insira um valor valido!')
    except ValueError: # Exceção de erro para a tentativa:
        print('⚠︎ Insira um valor valido!')

# Remover estabelecimento:
def remover_estabelecimento(lista):
    # Listamos os estabelecimentos para que o usuario possa escolher oque deseja alterar o estado:
    listar_restaurantes(lista)
    # Caso não tenha nenhum 
    if not lista:
        return
    # Caso tenha, tentar:
    try:
        # Usuario escolhe o estabelecimento alvo da lista:
        rest_alvo = int(input('▶ Digite o número do estabelecimento em que deseja remover: '))
        # Se numero alvo do estabelecimento for menor que 0
        if 0 < rest_alvo <= len(lista):
            print('⋄ Você confirma sua escolha S para SIM ou N para NÃO, LEMBRE-SE NÃO É POSSÍVEL REVERTER')
            escolha = input('▶ Escolha: ').lower()
            if escolha == 's':
                # Usamos rest_alvo - 1 pois o for começa do 0
                estabelecimento_removido = lista.pop(rest_alvo - 1)
                print(f'⋄ O estabelecimento "{estabelecimento_removido.nome}" foi removido com SUCESSO! ✓')
            elif escolha == 'n':
                print('⋄ Cancelando...')
            else:
                print('⚠︎ Insira um valor valido!')
    except ValueError:
        print('⚠︎ Insira um valor valido!')

# Nome do Programa:
def nome_programa():
    print('''
         Ｓｔｏｒｅ　Ｍａｎａｇｅｒ
         ✦•┈๑⋅⋯ ( ˶ˆ꒳ˆ˵ ) ⋯⋅๑┈•✦ ''')

# Opções Inico:
def opcoes_inicio():
    print('┏━╾──────────────────────────────────╼━┓')
    print('┃〔 1  ＋Cadastrar restaurantes      〕┃')
    print('┃〔 2  ☰ Listar Restaurantes         〕┃')
    print('┃〔 3  ☲ Opções                      〕┃')
    print('┃〔 4  ⤾ Sair do aplicativo          〕┃')
    print('┗━╾──────────────────────────────────╼━┛')

# Opções para as opções:
def opcoes_opcoes(restaurantes):
    while True:
        print('┏━╾──────────────────────────────────────────╼━┓')
        print('┃〔 1  ✎  Alterar o estado de funcionamento  〕┃')
        print('┃〔 2  ✗  Deletar um estabelecimento         〕┃')
        print('┃〔 3  ⇦  Voltar ao menu principal           〕┃')
        print('┗━╾──────────────────────────────────────────╼━┛')
        
        escolha = input('▶ Sua escolha é: ')
        if e_numero(escolha):
            escolha = int(escolha)
            match escolha:
                case 1:
                    alterar_status(restaurantes)
                case 2:
                    remover_estabelecimento(restaurantes)
                case 3:
                    # Sair do loop e voltar ao menu principal
                    break
                case _:
                    print('⚠︎ Opção invalida, tente novamente!')
        else:
            print('⚠︎ Insira um número correspondente a uma opção válida!')

# Main:
def main():
    restaurantes = []
    while True:
        nome_programa()
        opcoes_inicio()
        escolha_opcao = input('▶ Sua escolha é: ')
        if e_numero(escolha_opcao):
            escolha_opcao = int(escolha_opcao)
            match escolha_opcao:
                case 1:
                    cadastrar_restaurantes(restaurantes)
                case 2:
                    listar_restaurantes(restaurantes)
                case 3:
                    opcoes_opcoes(restaurantes)
                case 4:
                    print('⋄ Saindo.....')
                    return  # Sair da função main e terminar o programa:
                case _:
                    print('⚠︎ Alerta! Insira um número valido de 1 a 4 e tente novamente!')
        else:
            print('⚠︎ Alerta! Insira um número valido de 1 a 4 e tente novamente!')

# Chamamos main:
if __name__ == '__main__': # Nem precisa dessa linha, pode deixar só a main()
    main()
