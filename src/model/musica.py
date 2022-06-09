class Musica:
    id: int
    nome: str
    aval: int

    def __init__(self, _id: int, nome: str, aval: int = 0):
        self.id = _id
        self.nome = nome
        self.aval = aval

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'aval': self.aval
        }
