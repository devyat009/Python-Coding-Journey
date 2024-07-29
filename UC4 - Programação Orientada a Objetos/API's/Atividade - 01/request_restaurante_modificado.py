# Atividade: Acesse um json de restaurantes com cardapios, valores e descrições.
# Trate estes dados e salve em arquivos diferentes para cada restaurante.
# Data: 22/07/2024
# Autor: Higor Stanley aka Devyat009
# Instrutor: Celso Brunno
import requests
import json
import os
import shutil

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
if response.status_code == 200:
    information_json = response.json()
    dados_restaurante = {}

    for item in information_json:
        restaurante = item['Company']
        produto = item['Item']
        valor = item['price']
        descricao = item['description']

        if restaurante not in dados_restaurante:
            dados_restaurante[restaurante] = []
        dados_restaurante[restaurante].append({'Item': produto, 'Valor': valor, 'Descricao': descricao})

    # Caminho das pastas
    caminho_pasta = 'output_files/restaurante_dump_tratado/'
    try:
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta, exist_ok=True)
            print(f"Pasta '{caminho_pasta}' criada.")
            
        else:
            print(f"Pasta '{caminho_pasta}' ja existe.")

        for nome_restaurante, dados in dados_restaurante.items():
            nome_do_arquivo = f'{nome_restaurante}.json'

            with open(nome_do_arquivo, 'w') as arquivo_restaurante:
                json.dump(dados, arquivo_restaurante,
                        indent = 4)
            shutil.move(nome_do_arquivo, caminho_pasta) # Move para a pasta criada
    except OSError as error:
        print(f'Error: {error}')
else:
    print(f"Ocorreu um erro de conexão: {response.status_code}")
