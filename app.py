from flask import Flask, request, jsonify, redirect, url_for, abort
from flask_migrate import Migrate
from utils import db
from models.mensagem import Mensagem
from controllers.mensagem import bp_mensagens

app = Flask(__name__)
app.register_blueprint(bp_mensagens, url_prefix='/mensagens')

app.config['SECRET_KEY'] = 'teste'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.errorhandler(400)
def conteudo_vazio(error):
    return jsonify({"mensagem":"Mensagem vazia."}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"mensagem":"Mensagem não encontrada."}), 404

@app.route('/')
def index():
    return "<a href='/mensagens'>/mensagens</a>"

if __name__ == '__main__':
    app.run()