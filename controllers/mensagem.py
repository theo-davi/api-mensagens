from flask import request, jsonify, abort, Blueprint
'''
do pacote (framework) flask, são importados:
- o objeto request, que representa uma requisição feita.
- a função abort, que interrompe a execução da requisição atual / da aplicação / do servidor, e retorna um código HTTP específico. Funciona aliada ao @errorhandler, já que
o @errorhandler manipula o erro, e é como se o abort chamasse o erro.
- a classe Blueprint, usada para modularizar a aplicação, ou seja, separá-la em módulos, que, normalmente, representam  rotas e operações que envolvem as tabelas
do banco de dados. Assim, pode-se criar uma pasta para agrupar esses módulos (no caso, a pasta controllers); cada módulo (feito para cada tabela do banco de dados) tem as
rotas com operações (ex.: CRUD) para suas respectivas tabelas.
'''
from models.mensagem import Mensagem
#importa, do módulo mensagem na pasta models, a classe Mensagem (que é o model da tabela mensagem no banco de dados, que a representa)
from utils import db

bp_mensagens = Blueprint("mensagens", __name__)
#cria uma instância de Blueprint com o nome interno "mensagens", que é o seu identificador único, usado para gerar endpoints (identificadores de funções decoradas das rotas),
# como mensagens.read_all; a variável bp_mensagens armazena o blueprint "mensagens". O parâmetro __name__ indica o módulo atual.

@bp_mensagens.route('/')#rota raiz ('/mensagens/' ou '/mensagens')
#a função decoradora @route registra, no Blueprint bp_mensagens, a função read_all como manipuladora da URL '/', que, nesse caso, é '/mensagens/'.
def read_all():
#define a função read_all (que foi decorada com o decorador route)
    global mensagens#declara a variável mensagens como global para poder ser acessada em outras funções
    mensagens=[]#atribui uma lista vazia à variável mensagens
    mensagens_bd=Mensagem.query.all()#recupera (consulta) todos os registros na tabela Mensagens do banco de dados e retorna em forma de lista
    for mensagem_bd in mensagens_bd:#itera sobre a lista mensagens_bd, que são todas as mensagens no banco de dados
        mensagens.append({
            "id":mensagem_bd.id,
            "conteudo":mensagem_bd.conteudo
        })#adiciona à lista mensagens, que é uma variável global, um item que é um dicionário, que tem a chave id com valor sendo o id da mensagem iterada do banco de dados e
# a chave conteudo com valor sendo o conteudo da mensagem iterada do banco de dados. Resumindo, cada mensagem no banco de dados é adicionada à variável (lista) mensagens.
    return jsonify({"mensagens":mensagens})#retorna um dicionário Python convertido em JSON com chave "mensagens" e o valor sendo a lista de mensagens que contém itens
#que são dicionários: as mensagens propriemante ditas.

@bp_mensagens.route('/', methods=['POST'])
#define que a função create está associada à rota '/mensagens/' apenas com o método POST (para criar recursos, dados, registros), ou seja, a função create é chamada quando
# for feita uma requisição POST à rota.
def create():
    mensagem=request.get_json().get("conteudo")#recupera os dados enviados no corpo da requisição como JSON e extrai o valor da chave "conteudo", que é o conteúdo da mensagem
    if mensagem=="":
        abort(400)#se a mensagem estiver vazia, a execução da aplicação é interrompida, retornando o código HTTP 400.
    mensagem_bd=Mensagem(mensagem)
    db.session.add(mensagem_bd)#adiciona a variável à sessão do banco de dados (adiciona a mensagem nova ao banco de dados)
    db.session.commit()#salva a nova mensagem no banco de dados
    return jsonify({"mensagem":"Mensagem criada."})#retorna um dicionário Python convertido em JSON com chave "mensagem" de valor "Mensagem criada.", que é uma resposta à
# requisição.

@bp_mensagens.route('/<int:id>')
def read_one(id):
    for mensagem in mensagens:
        if mensagem['id']==id:
            return mensagem
    abort(404)

@bp_mensagens.route('/<int:id>', methods=['PUT'])
def update(id):
    for mensagem in mensagens:
        if mensagem['id']==id:
            if request.get_json().get('conteudo')=="":
                abort(400)                    
            mensagem_bd=Mensagem.query.get(id)#recupera (consulta) e retorna como objeto o registro na tabela Mensagens do banco de dados de acordo com o id
            mensagem_bd.conteudo=request.get_json().get('conteudo')
            db.session.add(mensagem_bd)
            db.session.commit()
            mensagem['conteudo']=request.get_json().get('conteudo')
            return jsonify({"mensagem":"Mensagem atualizada."})
    abort(404)

@bp_mensagens.route('/<int:id>', methods=['DELETE'])
def delete(id):
    mensagem_bd=Mensagem.query.get(id)
    if mensagem_bd:
        db.session.delete(mensagem_bd)
        db.session.commit()
        return jsonify({"mensagem":"Mensagem deletada."})
    abort(404)