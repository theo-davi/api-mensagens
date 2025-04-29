from flask import render_template, request, redirect, flash, url_for
from models.Usuario import Usuario
from utils import db
from flask import Blueprint

bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')

@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('usuarios_create.html')
    
    elif request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        csenha = request.form['csenha']
        
        usuario = Usuario(nome, email, senha)
        db.session.add(usuario)
        db.session.commit()
        flash('Dados inseridos com sucesso', 'success')
        return redirect(url_for('usuarios.recovery'))

@bp_usuarios.route('/recovery', defaults={'id': 0})
@bp_usuarios.route('/recovery/<int:id>')
def recovery(id):
    if (id==0):
        usuarios = Usuario.query.all()
        return render_template('usuarios_recovery.html', usuarios=usuarios)
    else:
        usuario = Usuario.query.get(id)
        return render_template('usuarios_detalhes.html', usuario=usuario)