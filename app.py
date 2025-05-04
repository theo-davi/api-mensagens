from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
import json
from flask_migrate import Migrate
from utils import db
from models.Mensagem import Mensagem

app = Flask(__name__)

app.config['SECRET_KEY'] = 'chave_secreta'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

arquivo=open('db.json')
dados=json.load(arquivo)
lista_mensagens=dados['mensagens']

'''dados['mensagens'] é uma lista de mensagens'''
'''mensagem é um dicionário'''

@app.route('/')
def index():
    return "<a href='/mensagens'>/mensagens</a>"

@app.route('/mensagens')
def read_all():
    mensagens=Mensagem.query.all()
    for mensagem in mensagens:
        lista_mensagens.append({"id":mensagem.id, "conteudo":mensagem.conteudo})
    return dados

@app.route('/mensagens/<id>')
def read_one(id):
    for mensagem in dados['mensagens']:
        if mensagem['id']==id:
            return mensagem
        else:
            return 'Esse ID não existe.'

@app.route('/mensagens', methods=['POST'])
def create():
    dados['mensagens'].append({"id":"5", "conteudo":"texto da nova mensagem"})
    return dados

@app.route('/mensagens/<id>', methods=['PUT'])
def update(id):
    for mensagem in dados['mensagens']:
        if mensagem['id']==id:
            mensagem.update({'conteudo':'novo texto da mensagem'})
            return mensagem
        else:
            return 'Esse ID não existe.'

@app.route('/mensagens/<id>', methods=['DELETE'])
def delete(id):
    for mensagem in dados['mensagens']:
        if mensagem['id']==id:
            dados['mensagens'].remove(mensagem)
            return dados
        else:
            return 'Esse ID não existe.'