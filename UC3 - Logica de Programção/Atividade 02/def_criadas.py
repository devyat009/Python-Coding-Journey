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

# Função para dizer qual é o tipo de terreno:
def tipo(string):
    try:
        if string <= 100:
            return "TERRENO POPULAR"
        elif 100 > string < 500:
            return "TERRENO MASTER"
        elif string >= 500:
            return "TERRENO VIP"
    except ValueError:
        False

# Função para checar se o ano inserido é bissexto:
def bissexto(string):
    try: 
        # Caso termine em '0' retorna verdadeiro:
        if str(string).endswith("0"):
            return True
        # Caso seja divisível por '4' retorna verdadeiro:
        elif int(string) % 4 == 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
    
# Função de identificar o sexo:
def sexu(string):
    try:
        string.lower
        if string.isalpha():
            if string == 'feminino' or string == 'mulher' or string == 'masculino' or string == 'homem':
                return True
        else:
            return False
    except ValueError:
        return False

# Como sao chamadas

# e numero
if e_numero(string):
    print("e uma letra")
else:
    print("nao e uma letra")

# e letra
if e_letra(string):
    print("e uma letra")
else:
    print("nao e uma letra")

# tipo
m2 = 150
tipa = tipo(m2)
print(tipa)

# bisseexto
if bissexto(ano):
    print("O ano é bissexto.")
else:
    print("Não é um ano bissexto.")
    
# Sexo
if sexu(sexo):
    sexo.lower
    if sexo == 'feminino':
        print('Valido')
    elif sexo == 'masculino':
else:
    print('Sexo invalido, digite feminino ou masculino')