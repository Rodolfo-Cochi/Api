class MusicaRepetidaException(Exception):
    def __init__(self, nome: str):
        self.message = f"O nome '{nome}' já existe na base"
        super().__init__(self.message)
