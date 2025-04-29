from flask import Flask, render_template, redirect, url_for, flash , request
from models import Mensagem
from utils import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'api-mensagens'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('create.html')
    elif request.method == "POST":
        conteudo = request.form['conteudo']
        mensagem = Mensagem(conteudo)
        db.session.add(mensagem)
        db.session.commit()
        flash('Dados inseridos com sucesso', 'success')

@app.route('/recovery', defaults={'id': 0})
@app.route('/recovery/<int:id>')
def recovery(id):
    if (id==0):
        mensagens = Mensagem.query.all()
        return render_template('recovery.html', mensagens=mensagens)
    else:
        mensagem = Mensagem.query.get(id)
        return render_template('detalhes.html', mensagem=mensagem)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if id and request.method=='GET':
        mensagem=Mensagem.query.get(id)
        return render_template('update.html', mensagem=mensagem)
    if request.method=='POST':
        mensagem = Mensagem.query.get(id)
        mensagem.conteudo = request.form['conteudo']
        db.session.add(mensagem)
        db.session.commit()
        flash('Dados inseridos com sucesso', 'success')
        return redirect(url_for('recovery', id=id))

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'GET':
        mensagem = Mensagem.query.get(id)
        return render_template('delete.html', mensagem = mensagem)
    if request.method=='POST':
        mensagem = Mensagem.query.get(id)
        db.session.delete(mensagem)
        db.session.commit()
        return redirect(url_for('recovery'))