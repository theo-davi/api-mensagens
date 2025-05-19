from flask import Flask, request, jsonify, redirect, url_for, abort
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

@app.errorhandler(400)
def conteudo_vazio(error):
    return jsonify({"mensagem":"Mensagem vazia."}), 400

@app.route('/')
def index():
    return "<a href='/mensagens'>/mensagens</a>"

@app.route('/mensagens')
def read_all():
    global mensagens
    mensagens=[]
    mensagens_bd=Mensagem.query.all()
    for mensagem_bd in mensagens_bd:
        mensagens.append({
            "id":mensagem_bd.id,
            "conteudo":mensagem_bd.conteudo
        })
    return jsonify({"mensagens":mensagens})

@app.route('/mensagens', methods=['POST'])
def create():
    mensagem=request.get_json().get("conteudo")
    if mensagem=="":
        abort(400)
    mensagem_bd=Mensagem(mensagem)
    db.session.add(mensagem_bd)
    db.session.commit()
    return redirect(url_for('read_all'))

@app.route('/mensagens/<int:id>')
def read_one(id):
    try:
        for mensagem in mensagens:
            if mensagem['id']==id:
                return mensagem
    except:
        return jsonify({"mensagem":"Mensagem não encontrada"}), 404

@app.route('/mensagens/<int:id>', methods=['PUT'])
def update(id):
    try:
        for mensagem in mensagens:
            if mensagem['id']==id:
                mensagem_bd=Mensagem.query.get(id)
                mensagem_bd.conteudo=request.get_json().get('conteudo')
                db.session.add(mensagem_bd)
                db.session.commit()
                mensagem['conteudo']=request.get_json().get('conteudo')
    except:
        return jsonify({"mensagem":"Mensagem não encontrada"}), 404
    else:
        return redirect(url_for('read_one', id=id))

@app.route('/mensagens/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        db.session.delete(Mensagem.query.get(id))
        db.session.commit()
        return redirect(url_for('read_all'))
    except:
        return jsonify({"mensagem":"Mensagem não encontrada"}), 404

if __name__ == '__main__':
    app.run()