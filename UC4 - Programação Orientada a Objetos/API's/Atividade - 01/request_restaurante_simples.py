# Atividade: Acesse um json de restaurantes com cardapios, valores e descrições e salve no computador.
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
    info = response.json()
    caminho_pasta = 'output_files/restaurante_dump_simples'
    try:
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta, exist_ok=True)
            print(f"Pasta '{caminho_pasta}' criada.")
        else:
            print(f"Pasta '{caminho_pasta}' ja existe.")
        # Nome do arquivo
        nome_arquivo = f'restaurante_simples.json'
        # Criacao do arquivo
        with open(nome_arquivo, 'w') as arquivo_restaurante:
                json.dump(info, arquivo_restaurante, indent= 4)
        # Mover o arquivo para o caminho definido
        shutil.move(nome_arquivo, caminho_pasta)
    except OSError as error:
        print(f'Error: {error}')
# Resposta de erro caso status code nao seja 200
else:
    print(f"Ocorreu um erro: {response.status_code}")