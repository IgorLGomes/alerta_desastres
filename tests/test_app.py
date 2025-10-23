from fastapi.testclient import TestClient

from alerta_desastres.app import app

client = TestClient(app)
HTTP_OK = 200


def test_root_status_and_message():
    resp = client.get("/")
    assert resp.status_code == HTTP_OK
    assert resp.json() == {"message": "Olá Mundo!"}


def test_root_payload():
    resp = client.get("/")
    assert resp.json() == {"message": "Olá Mundo!"}
3