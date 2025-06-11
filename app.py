from flask import Flask, jsonify, render_template_string
'''
do pacote (framework) flask, são importados:
- a classe Flask, sua principal, usada para criar uma aplicação web com Python;
- a função jsonify, usada para converter dicionários Python em respostas no formato JSON;
- a função render_template_string, usada para renderizar templates HTML a partir de strings.
'''
from flask_migrate import Migrate
#importa, do pacote flask_migrate, a classe Migrate, que gerencia *migrações* (envio de models para se tornarem tabelas e atualizarem o banco de dados) de banco de dados
# em apps com SQLAlchemy. Com a Migrate, atualiza-se models (que representam tabelas do banco de dados) e versiona-se as alterações. Ele facilita o trabalho do Alembic.
from utils import db
#importa, do módulo utils, a variável db.
from controllers.mensagem import bp_mensagens
#importa, do módulo mensagem da pasta controllers, a variável bp_mensagens.

app = Flask(__name__)
#cria uma instância da classe Flask, ou seja, cria a aplicação web Flask.
app.register_blueprint(bp_mensagens, url_prefix='/mensagens')
#registra o blueprint bp_mensagens na aplicação e define um prefixo comum para todas as rotas do bp, começando com /mensagens.

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
#define nas configurações da aplicação que o caminho do banco de dados do SQLAlchemy, que é SQLITE, está no mesmo diretório do projeto (diretório raiz), e o arquivo do bd
# é project.db. Ou seja, configura o caminho do banco de dados na estrutura de diretórios do projeto Flask.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#define nas configurações da aplicação a desativação do monitoramento de modificações do SQLAlchemy. Ele monitora modificações nos objetos (nas instâncias, e não nos models)
# do banco de dados para emitir avisos sobre eles, como em criação de dados. Esse monitoramento está sendo desativado para poupar memória, já que não é desejo da aplicação
# atual.

db.init_app(app)
#conecta o banco de dados com a aplicação.
migrate = Migrate(app, db)
#conecta as migrações do Flask Migrate à aplicação e ao banco de dados criados (instanciados).

@app.errorhandler(400)
#a função decoradora errorhandler registra a função conteudo_vazio como manipuladora do erro 400 na aplicação, ou seja, sempre que houver o erro 400, a função
# conteudo_vazio vai ser chamada.
def conteudo_vazio(error):
    '''
        essa função r
    '''
    return jsonify({"mensagem":"Mensagem vazia."}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"mensagem":"Mensagem não encontrada."}), 404

@app.route('/')
def index():
    return render_template_string('''<a href="{{url_for('mensagens.read_all')}}">/mensagens</a>''')

if __name__ == '__main__':
    app.run()