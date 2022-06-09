import os
import pickle

from src.model.musica import Musica
from src.repo.errors.MusicaNotFound import MusicaNotFound
from src.repo.errors.MusicaRepetidaException import MusicaRepetidaException


class Db:
    DB_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'musicas.pkl')

    def __init__(self):
        try:
            with open(self.DB_PATH, 'rb') as file:
                self.musicas = pickle.load(file)
        except FileNotFoundError:
            self.musicas = []
            self.save_musicas()

    def save_musicas(self):
        with open(self.DB_PATH, 'wb') as file:
            pickle.dump(self.musicas, file)

    def get_counter(self):
        return len(self.musicas)

    def get_musica_por_nome(self, nome: str):
        for musica in self.musicas:
            if musica.nome == nome:
                return musica
        raise MusicaNotFound(nome=nome)

    def sort_musicas(self):
        musicas_0 = []
        musicas_1 = []
        musicas_2 = []
        musicas_3 = []
        musicas_4 = []
        musicas_5 = []
        for musica in self.musicas:
            if musica.aval == 0:
                musicas_0.append(musica)
            elif musica.aval == 1:
                musicas_1.append(musica)
            elif musica.aval == 2:
                musicas_2.append(musica)
            elif musica.aval == 3:
                musicas_3.append(musica)
            elif musica.aval == 4:
                musicas_4.append(musica)
            elif musica.aval == 5:
                musicas_5.append(musica)

        musicas_0.sort(key=lambda m: m.nome)
        musicas_1.sort(key=lambda m: m.nome)
        musicas_2.sort(key=lambda m: m.nome)
        musicas_3.sort(key=lambda m: m.nome)
        musicas_4.sort(key=lambda m: m.nome)
        musicas_5.sort(key=lambda m: m.nome)

        self.musicas = [
            *musicas_5,
            *musicas_4,
            *musicas_3,
            *musicas_2,
            *musicas_1,
            *musicas_0
        ]

        self.save_musicas()

    def cadastrar(self, nome: str):
        nome = nome.lower()

        for musica in self.musicas:
            if musica.nome == nome:
                raise MusicaRepetidaException(nome=nome)

        musica = Musica(_id=self.get_counter(), nome=nome)
        self.musicas.append(musica)

        self.sort_musicas()
        self.save_musicas()

        return musica

    def listar(self):
        return self.musicas

    def aval(self, nome: str, aval: int):
        nome = nome.lower()

        if aval < 1:
            aval = 1
        elif aval > 5:
            aval = 5

        musica = self.get_musica_por_nome(nome=nome)
        musica.aval = aval
        self.sort_musicas()
        self.save_musicas()
        return musica

    def clear(self):
        if os.path.exists(self.DB_PATH):
            os.remove(self.DB_PATH)
            self.__init__()
