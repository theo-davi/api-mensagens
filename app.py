from flask import Flask, jsonify, render_template_string
'''
do pacote (framework) flask, são importados:
- a classe Flask, sua principal, usada para criar uma aplicação web com Python;
- a função jsonify, usada para converter dicionários Python em respostas no formato JSON;
- a função render_template_string, usada para renderizar templates HTML a partir de strings.
'''
from flask_migrate import Migrate
#importa, do pacote flask_migrate, a classe Migrate, que gerencia *migrações* (envio de models para se tornarem tabelas) de banco de dados em apps
#com SQLAlchemy. Com a Migrate, atualiza-se models (que representam tabelas do banco de dados) e versiona-se as alterações.
from utils import db
#importa, do módulo utils, a variável db.
from controllers.mensagem import bp_mensagens

app = Flask(__name__)
#cria uma instância da classe Flask, ou seja, cria a aplicação web Flask.
app.register_blueprint(bp_mensagens, url_prefix='/mensagens')
#registra o blueprint bp_mensagens na aplicação e define um prefixo comum para todas as rotas do bp, começando com /mensagens.

app.config['SECRET_KEY'] = 'teste'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)#conecta o banco de dados com a aplicação.
migrate = Migrate(app, db)

@app.errorhandler(400)
def conteudo_vazio(error):
    return jsonify({"mensagem":"Mensagem vazia."}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"mensagem":"Mensagem não encontrada."}), 404

@app.route('/')
def index():
    return render_template_string('''<a href="{{url_for('mensagens.read_all')}}">/mensagens</a>''')

if __name__ == '__main__':
    app.run()