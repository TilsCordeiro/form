from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "media": None, "mensagem": None})

@app.post("/calcular", response_class=HTMLResponse)
async def calcular_media(request: Request, nota1: float = Form(...), nota2: float = Form(...)):
    media = (nota1 + nota2) / 2
    mensagem = "Aluno aprovado!" if media >= 7 else "Aluno reprovado."
    return templates.TemplateResponse("index.html", {"request": request, "media": media, "mensagem": mensagem})

