# Requisitar as informações da api: 
# Retornar as chaves modificadas para uma pagina localhost
# env
# .\"UC5 - Interfaces\HtmlSites\env\Scripts\activate.bat"
# Para executar o arquivo:
# No Bash:
# Navegue ate o arquivo
# cd UC5\ -\ Interfaces/HtmlSites
# $ fastapi dev MainApi.py
# No CMD:
# cd "UC5 - Interfaces\HtmlSites"
# uvicorn MainApi:read_page --reload
# Ou
# uvicorn MainApi:read_page --reload --factory

# Paginas Acessiveis:
# http://127.0.0.1:8000/api/xx
# http://127.0.0.1:8000/api/xx
# http://127.0.0.1:8000/

from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
import requests
# Import Validadors
from app.functions.validadors import validator
from app.functions.errorhandler import errorhandler
# Import DB
from app.db.db import DataBase
# Import entities models
from app.entities.CadastroModel import CadastroData

import os
from fastapi.responses import HTMLResponse
app = FastAPI(title="Custom FastAPI")

# Retornar uma pagina HTML simples.
@app.get("/", tags=["Redirect"])
def read_page():
    '''
    Pagina Simples para redirecionar as outras URL's
    '''
    with open(os.path.join(os.path.dirname(__file__), 'app/mainPage/main.html'), encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content=content)


app.mount("/static/aula01", StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'app', 'aula01')), name="static_aula01")
@app.get("/aula01", tags=["Aula 01"])
def aula01_page():
    with open(os.path.join(os.path.dirname(__file__), 'app/aula01/aula01.html'), encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content=content)

app.mount("/static/aula02", StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'app', 'aula02')), name="static_aula02")
@app.get("/aula02", tags=["Aula 02"])
def aula01_page():
    with open(os.path.join(os.path.dirname(__file__), 'app/aula02/aula02.html'), encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content=content)

app.mount("/static/aula03", StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'app', 'aula03')), name="static_aula03")
@app.get("/aula03", tags=["Aula 03"])
def aula01_page():
    with open(os.path.join(os.path.dirname(__file__), 'app/aula03/aula03.html'), encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.post("/test", tags=["Test"])
def test(data: CadastroData):
    try:
        v = validator()
        v.validate_email(data.email)
        v.validate_password(data.senha)
        v.validate_telefone(data.telefone)
        db = DataBase()
        cursor = db.connection.cursor()
        cursor.execute(
            "INSERT INTO userdb (nome, telefone, email, usuario, senha) VALUES (?, ?, ?, ?, ?)",
            (data.nome, data.telefone, data.email, data.usuario, data.senha)
        )
        db.connection.commit()

        return {"success": True, "message": "Data validated and stored!"}

    except errorhandler as e:
        raise HTTPException(status_code=400, detail={"errors": e.errors})