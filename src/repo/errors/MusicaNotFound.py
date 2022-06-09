class MusicaNotFound(Exception):
    def __init__(self, nome: str):
        self.message = f"O nome '{nome}' não foi encontrado na base"
        super().__init__(self.message)
