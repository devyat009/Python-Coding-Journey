# Requisitar as informações da api: https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json
# Retornar as chaves modificadas para uma pagina localhost

# Para executar o arquivo:
# No Bash:
# $ fastapi dev FastAPI.py
# No CMD:
# uvicorn FastAPI:read_page

# Paginas Acessiveis:
# http://127.0.0.1:8000/api/restaurante
# http://127.0.0.1:8000/api/restaurante2
# http://127.0.0.1:8000/

from fastapi import FastAPI, Query
import requests

import os
from fastapi.responses import HTMLResponse
app = FastAPI()

# Retornar uma pagina HTML simples.
@app.get("/")
def read_page():
    '''
    Pagina Simples para redirecionar as outras URL's
    '''
    with open(os.path.join(os.path.dirname(__file__), 'page.html')) as f:
        content = f.read()
    return HTMLResponse(content=content)


# Mostrar as informações de 1 unico restaurante
@app.get("/api/restaurante")
def mostrar_cardapio():
    '''
    Mostrar o cardapio de um unico restaurante, o KFC.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        dados_restaurante = []

        for item in info:
            if item['Company'] == 'KFC':
                dados_restaurante.append({
                'item': item['Item'],
                'preco':item['price'],
                'descricao': item['description']
                })
        return {'KFC':dados_restaurante}
    else:
        print('Algo ocorreu de errado ao tentar entrar em contato com a API externa')

# Mostrar as informações de varios restaurantes.
@app.get("/api/restaurante2")
def mostrar_cardapio(restaurante: str = Query(None)):
    '''
    Mostrar cardapio por restaurante.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if response.status_code == 200:
        info = response.json()
        dados_restaurante = []
        if restaurante is None:
            return {'Informações': info}
        for item in info:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                'item': item['Item'],
                'preco':item['price'],
                'descricao': item['description']
                })
        # Retorna as informções
        return {'Restaurante': restaurante,
                'Cardapio': dados_restaurante}
    else:
        print('Algo ocorreu de errado ao tentar entrar em contato com a API externa')