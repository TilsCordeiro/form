from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_formulario_get():
    response = client.get("/")
    assert response.status_code == 200
    assert "<form" in response.text

def test_calcular_media_aprovado():
    response = client.post("/calcular", data={"nota1": 8, "nota2": 9})
    assert response.status_code == 200
    assert "Aluno aprovado!" in response.text
    assert "8.5" in response.text

def test_calcular_media_reprovado():
    response = client.post("/calcular", data={"nota1": 5, "nota2": 6})
    assert response.status_code == 200
    assert "Aluno reprovado." in response.text
    assert "5.5" in response.text

def test_calcular_media_limite_aprovacao():
    response = client.post("/calcular", data={"nota1": 7, "nota2": 7})
    assert response.status_code == 200
    assert "Aluno aprovado!" in response.text
    assert "7.0" in response.text

def test_formulario_com_nota_faltando():
    response = client.post("/calcular", data={"nota1": 7})
    assert response.status_code == 422
