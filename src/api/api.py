from flask import Flask, jsonify, request, Response
import src.config as config
from src.repo.errors.MusicaNotFound import MusicaNotFound
from src.repo.errors.MusicaRepetidaException import MusicaRepetidaException
from src.repo.pickle.db import Db


app = Flask(import_name=config.API_NAME)

db = Db()


@app.route('/')
def index():
    return jsonify({
            'name': config.API_NAME,
            'port': config.PORT
    })


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/cadastrar', methods=['PUT'])
def cadastrar():
    nome = request.json['nome']

    try:
        musica = db.cadastrar(nome=nome)
    except MusicaRepetidaException as err:
        return Response(f'{{"msg": "{err.message}"}}', status=400, mimetype='application/json')

    return jsonify(musica.to_json())


@app.route('/listar', methods=['GET'])
def listar():
    musicas = db.listar()
    return jsonify([musica.to_json() for musica in musicas])


@app.route('/aval', methods=['POST'])
def avaliar():
    nome = request.json['nome']
    aval = request.json['aval']

    try:
        musica = db.aval(nome=nome, aval=aval)
    except MusicaNotFound as err:
        return Response(f'{{"msg": "{err.message}"}}', status=404, mimetype='application/json')

    return jsonify(musica.to_json())


def run():
    print(f'API {config.API_NAME} rodando na porta {config.PORT}...')
    app.run(host='0.0.0.0', port="3000")
