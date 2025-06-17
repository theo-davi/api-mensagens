from flask import request, jsonify, abort, Blueprint
from models.mensagem import Mensagem
from utils import db
from sqlalchemy import desc

bp_mensagens = Blueprint("mensagens", __name__)

@bp_mensagens.route('/')
def read_all():
    mensagens=Mensagem.query.order_by(desc(Mensagem.id)).all()
    return jsonify({"mensagens":[mensagem.to_dict() for mensagem in mensagens]})

@bp_mensagens.route('/', methods=['POST'])
def create():
    dado=request.get_json()
    if not dado or dado['conteudo']=='':
        abort(400)
    nova_mensagem=Mensagem(conteudo=dado['conteudo'])
    db.session.add(nova_mensagem)
    db.session.commit()
    return jsonify({"mensagem":"Mensagem criada."}), 201

@bp_mensagens.route('/<int:id>')
def read_one(id):
    mensagem=Mensagem.query.get_or_404(id)
    return jsonify({"mensagem":mensagem.to_dict()})

@bp_mensagens.route('/<int:id>', methods=['PUT'])
def update(id):
    mensagem=Mensagem.query.get_or_404(id)
    dado=request.get_json()
    if not dado or dado['conteudo']=="":
        abort(400)                    
    mensagem.conteudo=dado['conteudo']
    db.session.commit()
    return jsonify({"mensagem":"Mensagem atualizada."})

@bp_mensagens.route('/<int:id>', methods=['DELETE'])
def delete(id):
    mensagem_bd=Mensagem.query.get_or_404(id)
    db.session.delete(mensagem_bd)
    db.session.commit()
    return jsonify({"mensagem":"Mensagem deletada."})