from flask import request, jsonify, abort, Blueprint
from models.mensagem import Mensagem
from utils import db

bp_mensagens = Blueprint("mensagens", __name__)

@bp_mensagens.route('/')
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

@bp_mensagens.route('/', methods=['POST'])
def create():
    mensagem=request.get_json().get("conteudo")
    if mensagem=="":
        abort(400)
    mensagem_bd=Mensagem(mensagem)
    db.session.add(mensagem_bd)
    db.session.commit()
    return jsonify({"mensagem":"Mensagem criada."})

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
            mensagem_bd=Mensagem.query.get(id)
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