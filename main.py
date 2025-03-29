from fastapi import FastAPI, Form #Capturar dados enviados
from fastapi.responses import HTMLResponse #Retornar páginas HTML
from fastapi.templating import Jinja2Templates #Usar templates HTML dinâmicos
from starlette.requests import Request #Requisição do usuário

app = FastAPI() #inicia
templates = Jinja2Templates(directory="templates") #define que os arquivos HTML estarão na pasta templates

@app.get("/", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "media": None, "mensagem":None})

@app.post("/calcular")
async def calcular_media(request: Request, nota1: float = Form(...), nota2: float = Form(...)):
    media = (nota1 + nota2) / 2
    mensagem = "Parabéns! Você foi aprovado!" if media > 5.9 else "Estude mais, você reprovou!"
    return templates.TemplateResponse("index.html", {"request": request, "media": media, "mensagem": mensagem})
