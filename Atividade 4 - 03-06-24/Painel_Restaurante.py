# Classe Restaurante
class Restaurante:
    def __init__(self, nome, categoria, status):
        self.nome = nome
        self.categoria = categoria
        self.status = status

# Função para cadastrar:
def cadastrar_restaurantes(restaurantes):
    nome = input('Digite o nome do restaurante: ')
    categoria = input('Digite qual é a categoria do restaurante (FastFood, Pizzaria, Restaurante): ')
    status = str(input('Qual o status do restaurante (Ativado ou Desativado): '))
    restaurante = Restaurante(nome, categoria, status)
    restaurantes.append(restaurante)  # adicionamos o estabelecimento à lista
    print('Cadastro realizado com SUCESSO!')

# Lista de Restaurantes:
def listar_restaurantes(restaurantes):
    # Caso não tenha nenhum estabelecimento:
    if not restaurantes:
        print('Não tem nenhum restaurante cadastrado')
        return
    # Imprimimos a lista de estabelecimento cadastrados:
    for i, restaurante in enumerate(restaurantes, start=1):
        print(f'Restaurante {i}: Nome: {restaurante.nome}, Categoria: {restaurante.categoria}, Status: {restaurante.status}')

# Alterar o Status
def alterar_status(restaurantes):
    # Listamos os estabelecimentos para que o usuario possa escolher oque deseja alterar o estado:
    listar_restaurantes(restaurantes)
    
    # Caso não tenha nenhum 
    if not restaurantes:
        return
    
    # Caso tenha, tentar:
    try:
        # Usuario escolhe o estabelecimento alvo da lista:
        rest_alvo = int(input('Digite o número do restaurante em que deseja alterar o estado: '))
        
        # Se numero alvo do estabelecimento for menor que 0
        if 0 < rest_alvo <= len(restaurantes):
            # Usuario inseri o novo estado:
            novo_status = input('Insira o novo status (Ativado ou Desativado): ')
            # Usamos rest_alvo - 1 pois o for começa do 0
            restaurantes[rest_alvo - 1].status = novo_status
            print('O estado do restaurante foi alterado com sucesso!')
        else:
            print('Insira um valor valido!')
    except ValueError:
        print('Insira um valor valido!')

def remover_estabelecimento(lista):
    # Listamos os estabelecimentos para que o usuario possa escolher oque deseja alterar o estado:
    listar_restaurantes(lista)
    
    # Caso não tenha nenhum 
    if not lista:
        return
    
    # Caso tenha, tentar:
    try:
        # Usuario escolhe o estabelecimento alvo da lista:
        rest_alvo = int(input('Digite o número do restaurante em que deseja remover: '))
        # Se numero alvo do estabelecimento for menor que 0
        if 0 < rest_alvo <= len(lista):
            print('Você confirma sua escolha S para SIM ou N para NÃO, LEMBRE-SE NÃO É POSSÍVEL REVERTER')
            escolha = input('Escolha: ').lower 
            if escolha == 's':
                # Usamos rest_alvo - 1 pois o for começa do 0
                estabelecimento_removido = lista.pop(rest_alvo - 1)
                print(f'O restaurante "{estabelecimento_removido.nome}" foi removido com sucesso!')
            elif escolha == 'n':
                print('Cancelando...')
            else:
                print('Insira um valor valido!')
    except ValueError:
        print('Insira um valor valido!')
    

# Nome do Programa:
def nome_programa():
    print('''                                                                                                               
  ____ _____ ____  _____ _   _  ____ ___    _    ____   ___  ____    ____  _   _ ____  ____  _____ __  __  ___  
 / ___| ____|  _ \| ____| \ | |/ ___|_ _|  / \  |  _ \ / _ \|  _ \  / ___|| | | |  _ \|  _ \| ____|  \/  |/ _ \ 
| |  _|  _| | |_) |  _| |  \| | |    | |  / _ \ | | | | | | | |_) | \___ \| | | | |_) | |_) |  _| | |\/| | | | |
| |_| | |___|  _ <| |___| |\  | |___ | | / ___ \| |_| | |_| |  _ <   ___) | |_| |  __/|  _ <| |___| |  | | |_| |
 \____|_____|_| \_|_____|_| \_|\____|___/_/   \_|____/ \___/|_| \_\ |____/ \___/|_|   |_| \_|_____|_|  |_|\___/ 
                                                                                                                
''')
    
# Opções:
def opcoes_inicio():
    print('\n Nome Provisorio')
    print('1 - Cadastrar restaurantes')
    print('2 - Listar Restaurantes')
    print('3 - Alterar Estado')
    print('4 - Sair do aplicativo')
    
# Main:
def main():
    restaurantes = []
    while True:
        
        nome_programa()
        opcoes_inicio()
        escolha_opcao = int(input('Sua escolha é: '))
        match escolha_opcao:
            case 1:
                cadastrar_restaurantes(restaurantes)
                
            case 2:
                listar_restaurantes(restaurantes)
            
            case 3:
                alterar_status(restaurantes)
            
            case 4:
                print('Saindo.....')
                break


if __name__ == '__main__':
    main()
