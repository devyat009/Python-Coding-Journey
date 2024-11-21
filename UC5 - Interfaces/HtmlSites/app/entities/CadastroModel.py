from pydantic import BaseModel
class CadastroData(BaseModel):
    nome: str
    telefone: str
    email: str
    usuario: str
    senha: str
