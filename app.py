from flask import Flask, request, jsonify
import json

app = Flask(__name__)

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
    arquivo=open('db.json', 'w')
    arquivo.write(json.dumps({"mensagens":mensagens}))
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
            arquivo=open('db.json', 'w')
            arquivo.write(json.dumps({"mensagens":mensagens}))
            return mensagem

@app.route('/mensagens/<int:id>', methods=['DELETE'])
def delete(id):
    for mensagem in mensagens:
        if mensagem['id']==id:
            mensagens.remove(mensagem)
            arquivo=open('db.json', 'w')
            arquivo.write(json.dumps({"mensagens":mensagens}))
            return jsonify({"mensagens":mensagens})