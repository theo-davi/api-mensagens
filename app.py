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
#registra o blueprint bp_mensagens na aplicação, anexando-o a ela, e define um prefixo comum para todas as rotas do bp, que vão começar com /mensagens.

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
#a função decoradora @errorhandler registra a função conteudo_vazio como manipuladora do erro 400 na aplicação. Em outras palavras, o decorador @errorhandler associa a função
# conteudo_vazio ao erro 400, ou seja, sempre que houver o erro de código 400, a função conteudo_vazio vai ser chamada. Resumindo, manipula o erro 400.
def conteudo_vazio(error):
#define uma função chamada conteudo_vazio que recebe como parâmetro obrigatório o objeto error, que contém detalhes do erro ocorrido, mesmo que esse objeto não seja usado
# depois; no caso, ele contém detalhes do erro 400.
    return jsonify({"mensagem":"Mensagem vazia."}), 400
'''
    a função conteudo_vazio (que pode ser chamada de decorada) retorna um dicionário Python convertido em JSON com a chave "mensagem" de valor "Mensagem vazia."
    e o código HTTP 400, que indica uma requisição mal-formada ou inválida; no caso, representa uma requisição feita com o conteúdo da mensagem vazio.
'''

@app.errorhandler(404)
#o erro 404 indica que o servidor não encontrou o recurso (dado) solicitado (requisitado); no caso, não encontrou a mensagem solicitada.
def not_found(error):
    return jsonify({"mensagem":"Mensagem não encontrada."}), 404
    #o segundo parâmetro do return serve para indicar o status HTTP da resposta e é opcional (usa-se quando se quer indicar o status HTTP da resposta), mas, por padrão,
    # retorna o código HTTP 200, que é para requisições bem-sucedidas, solicitações que foram atendidas pelo servidor.

@app.route('/')
#a função decoradora @route registra a função index como manipuladora da URL '/'; em outras palavras, o decorador @route registra a função index para a URL (rota) '/', ou
# seja, quando alguém acessar a rota '/' da minha aplicação, a função index é executada. Resumindo, define a rota '/' na aplicação.
def index():
    return render_template_string('''<a href="{{url_for('mensagens.read_all')}}">/mensagens</a>''')
    #renderiza a string como um template HTML para, assim, ser possível usar o url_for diretamente na string. Como a string é de aspas triplas, é possível usar aspas simples e
    # duplas dentro dela.

if __name__ == '__main__':
    app.run()#inicia o servidor de desenvolvimento da aplicação (executa a aplicação).
'''
    a aplicação só roda diretamente (que é quando o valor de __name__ é igual a __main__). Não roda se for importada em outro módulo. Serve para evitar que o servidor Flask
    rode acidentalmente quando, por exemplo, importa-se funções de um módulo que importou a aplicação.
'''