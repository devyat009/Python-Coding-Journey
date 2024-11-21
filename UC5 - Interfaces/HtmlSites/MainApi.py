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


app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'app', 'aula01')), name="static")
@app.get("/aula01", tags=["Aula 01"])
def aula01_page():
    with open(os.path.join(os.path.dirname(__file__), 'app/aula01/aula01.html'), encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.post("/test", tags=["Test"])
def test(data: CadastroData):
    try:
        v = validator()
        v.validate_email(data["email"])
        v.validate_password(data["password"])
        v.validate_telefone(data["telefone"])

        # Save to the database (simplified example)
        db = DataBase()
        cursor = db.connection.cursor()
        cursor.execute(
            "INSERT INTO userdb (nome, telefone, email, usuario, senha) VALUES (?, ?, ?, ?, ?)",
            ("Test User", data["telefone"], data["email"], "test_user", data["password"])
        )
        db.connection.commit()

        return {"success": True, "message": "Data validated and stored!"}

    except errorhandler as e:
        raise HTTPException(status_code=400, detail={"errors": e.errors})