from flask import Flask, render_template, request, redirect, flash, url_for
from utils import db
from flask_migrate import Migrate
from models.Mensagem import Mensagem

app = Flask(__name__)

app.config['SECRET_KEY'] = 'teste'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/mensagens', methods=['GET', 'POST'])
def mensagens():
    if request.method=='GET':
        return render_template('create.html')
    elif request.method=='POST':
        m=(request.form['conteudo'])
        mensagem=Mensagem(m)
        db.session.add(mensagem)
        db.session.commit()
        return redirect('recovery')

@app.route('/recovery', defaults={'id': 0})
@app.route('/recovery/<int:id>')
def recovery(id):
    if (id==0):
        mensagens = Mensagem.query.all()
        return render_template('recovery.html', mensagens=mensagens)