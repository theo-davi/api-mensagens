from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'teste'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

class Mensagem(db.Model):
    __tablename__="mensagem"
    id = db.Column(db.Integer, primary_key = True)
    conteudo = db.Column(db.String(280))

    def __init__(self, conteudo):
        self.conteudo = conteudo
    
    def __repr__(self):
        return "<Mensagem {}>".format(self.conteudo)

@app.route('/')
def index():
    return "<a href='/mensagens'>/mensagens</a>"

mensagens=[]
auto_id=1

@app.route('/mensagens', methods=['POST'])
def create():
    global auto_id
    mensagem={
        "id":auto_id,
        "conteudo":request.get_json().get("conteudo")
    }
    mensagens.append(mensagem)
    auto_id+=1
    db.session.add(Mensagem(request.get_json().get("conteudo")))
    db.session.commit()
    return jsonify({"mensagens":mensagens})

@app.route('/mensagens')
def read_all():
    return jsonify({"mensagens":mensagens})

@app.route('/mensagens/<int:id>')
def read_one(id):
    for mensagem in mensagens:
        if mensagem['id']==id:
            return mensagem
    return 'Mensagem não encontrada.'

@app.route('/mensagens/<int:id>', methods=['PUT'])
def update(id):
    for mensagem in mensagens:
        if mensagem['id']==id:
            mensagem['conteudo']=request.get_json().get('conteudo')
            return mensagem

@app.route('/mensagens/<int:id>', methods=['DELETE'])
def delete(id):
    for mensagem in mensagens:
        if mensagem['id']==id:
            mensagens.remove(mensagem)
            return jsonify({"mensagens":mensagens})