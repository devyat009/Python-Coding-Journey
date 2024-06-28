# Função para checar se o input do usuário é número inteiro:
def e_numeroint(string):
    if string.isnumeric():
        return True
    return False

# Função para checar se o input do usuário é número decimal:
def e_numerofloat(string):
    try:
        if string:
            float(string)
            return True
        else:
            return False
    except ValueError:
        return False


integer = input('Um numero inteiro: ')
if e_numeroint(integer):
    print('Verdadeiro')
else:
    print('Falso')

float = input('Um numero decimal: ')
if e_numerofloat(float):
    print('Verdadeiro')
else:
    print('Falso')