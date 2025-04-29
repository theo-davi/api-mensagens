from flask import Flask, render_template, redirect, url_for, flash , request
from utils import db
import os
from flask_migrate import Migrate
from models.Usuario import Usuario
from models.Pizza import Pizza
from controllers.Usuario import bp_usuarios
from controllers.Pizza import bp_pizzas

app = Flask(__name__)
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
app.register_blueprint(bp_pizzas, url_prefix='/pizzas')

app.config['SECRET_KEY'] = 'teste'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')