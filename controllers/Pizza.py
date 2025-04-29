from flask import render_template, request, redirect, flash, url_for
from models.Pizza import Pizza
from utils import db
from flask import Blueprint

bp_pizzas = Blueprint("pizzas", __name__, template_folder='templates')

@bp_pizzas.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('pizzas_create.html')
    
    elif request.method == "POST":
        sabor = request.form['sabor']
        imagem = request.form['imagem']
        ingredientes = request.form['ingredientes']
        preco = request.form['preco']
        
        pizza = Pizza(sabor, imagem, ingredientes, preco)
        db.session.add(pizza)
        db.session.commit()
        flash('Dados inseridos com sucesso', 'success')
        return redirect('recovery')

@bp_pizzas.route('/recovery', defaults={'id': 0})
@bp_pizzas.route('/recovery/<int:id>')
def recovery(id):
    if (id==0):
        pizzas = Pizza.query.all()
        return render_template('pizzas_recovery.html', pizzas=pizzas)
    else:
        pizza = Pizza.query.get(id)
        return render_template('pizzas_detalhes.html', pizza=pizza)

@bp_pizzas.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if id and request.method=='GET':
        pizza=Pizza.query.get(id)
        return render_template('pizzas_update.html', pizza=pizza)
    if request.method=='POST':
        pizza = Pizza.query.get(id)
        pizza.sabor = request.form['sabor']
        pizza.imagem = request.form['imagem']
        pizza.ingredientes = request.form['ingredientes']
        pizza.preco = request.form['preco']
        db.session.add(pizza)
        db.session.commit()
        flash('Dados inseridos com sucesso', 'success')
        return redirect(url_for('pizzas.recovery', id=id))

@bp_pizzas.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'GET':
        pizza = Pizza.query.get(id)
        return render_template('pizzas_delete.html', pizza = pizza)
    if request.method=='POST':
        pizza = Pizza.query.get(id)
        db.session.delete(pizza)
        db.session.commit()
        return redirect(url_for('pizzas.recovery'))