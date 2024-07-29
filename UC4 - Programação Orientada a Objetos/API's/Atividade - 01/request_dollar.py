# Atividade: Acesse o valor do dolar de uma api e print o valor do dolar.
# Data: 22/07/2024
# Autor: Higor Stanley aka Devyat009
# Instrutor: Celso Brunno
import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

response = requests.get(url)
if response.status_code == 200:
    informacoes_json = response.json()
    valor_dolar = informacoes_json['USDBRL']['bid']
    print(valor_dolar)