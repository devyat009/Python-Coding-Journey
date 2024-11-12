# Requisitar as informações da api: 
# Retornar as chaves modificadas para uma pagina localhost

# Para executar o arquivo:
# No Bash:
# Navegue ate o arquivo
# cd UC5\ -\ Interfaces/HtmlSites
# $ fastapi dev FastAPI.py
# No CMD:
# uvicorn FastAPI:read_page

# Paginas Acessiveis:
# http://127.0.0.1:8000/api/xx
# http://127.0.0.1:8000/api/xx
# http://127.0.0.1:8000/

from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
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
    with open(os.path.join(os.path.dirname(__file__), 'app/mainPage/main.html')) as f:
        content = f.read()
    return HTMLResponse(content=content)


app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'app/aula01')), name="static")
@app.get("/aula01")
def aula01_page():
    with open(os.path.join(os.path.dirname(__file__), 'app/aula01/aula01.html')) as f:
        content = f.read()
    return HTMLResponse(content=content)