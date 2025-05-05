from flask import Flask, redirect
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

arquivo=open('db.json', 'w')

@app.route('/')
def index():
    return "<a href='/mensagens'>/mensagens</a>"

@app.route('/mensagens')
def read_all():
    return json.load(open('db.json'))

@app.route('/mensagens/<id>')
def read_one(id):
    for mensagem in dados['mensagens']:
        if mensagem['id']==id:
            return mensagem
        else:
            return 'Esse ID não existe.'

@app.route('/mensagens', methods=['POST'])
def create():
    db.session.add(Mensagem('nova mensagem'))
    db.session.commit()
    arquivo.write(json.dumps({"id":"mensagem.id", "conteudo":"mensagem.conteudo"}))
    return redirect('mensagens')

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