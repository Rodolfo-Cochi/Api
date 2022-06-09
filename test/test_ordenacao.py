from src.repo.pickle.db import Db


def test_ordenacao():
    db = Db()

    db.clear()  # Deletando todas as entradas da DB

    db.cadastrar('Ziriguidum')
    db.cadastrar('Drive My Car')
    db.cadastrar('Avalanche')

    musicas = [musica.to_json() for musica in db.listar()]

    assert str(musicas) == "[{'id': 2, 'nome': 'avalanche', 'aval': 0}, {'id': 1, 'nome': 'drive my car', 'aval': 0}, {'id': 0, 'nome': 'ziriguidum', 'aval': 0}]"
