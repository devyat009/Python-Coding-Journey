# Atividade: Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
# aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
# carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
# que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
# quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
# tabela a seguir:
# - Carros populares (aluguel de R$90 por dia)
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km
# - Carros de luxo (aluguel de R$150 por dia)
# - Até 200Km percorridos: R$0,30 por Km
# - Acima de 200Km percorridos: R$0,25 por Km
# Data: 22/05/2024
# Instutor: Bruno
# Autor: Higor Stanley

# Mudar o valor baseado no carro
def carro_tipo(tipo: str, dia: int, km: float):
    tipo= str(tipo).lower()
    if tipo == 'popular':
        custo_dia = dia * 90 # 90 é o valor do dia para o carro popular
        if km <= 100:
            custo_km = km * 0.20
        elif km > 100:
            custo_km = km * 0.10
    elif tipo== 'luxo':
        custo_dia = dia * 150 # 150 é o valor do dia para o carro de luxo
        if km <= 200:
                custo_km = km * 0.30
        elif km > 200:
                custo_km = km * 0.25
    else:
        return "\nALERTA! Insira apenas uma das duas opções: Popular ou Luxo\n\nTente novamente:"
    return custo_dia + custo_km

# Programa em loop para validar o input:
while True:
    print(f'''Instruções: Insira os valores separados por ','\nExemplo: Luxo,8,150\n''')
    tipo, dia, km = input('''Escolha o tipo de carro: Popular ou Luxo e a quantidade de dias alugado e a quantidade de KM percoriddo:''').split(',')
    try:
        dia = int(dia)
        km = float(km)
        # Resultado da magimatica
        resultado = carro_tipo(tipo, dia, km)
        if isinstance(resultado, str):  # Verifica se o resultado é uma mensagem de erro
            print(resultado)
        else:
            print(f"O custo total é: R${resultado}")
            break 
    # Caso o input do usuário não seja números para dias e quilometragem:
    except ValueError:
        print("ALERTA! Insira valores válidos para os dias e quilometragem. Tente novamente!")