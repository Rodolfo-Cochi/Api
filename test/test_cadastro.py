from src.repo.pickle.db import Db


def test_ordenacao():
    db = Db()

    db.clear()  # Deletando todas as entradas da DB

    db.cadastrar('Drive My Car')

    musicas = [musica.to_json() for musica in db.listar()]

    assert str(musicas) == "[{'id': 0, 'nome': 'drive my car', 'aval': 0}]"
