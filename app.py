from flask import Flask, jsonify, render_template_string
from flask_migrate import Migrate
from utils import db
from controllers.mensagem import bp_mensagens

app = Flask(__name__)
app.register_blueprint(bp_mensagens, url_prefix='/mensagens')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.errorhandler(400)
def conteudo_vazio(error):
    return jsonify({"mensagem":"Mensagem vazia."}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"mensagem":"Mensagem não encontrada."}), 404

@app.route('/')
def index():
    return render_template_string('''<a href="{{url_for('mensagens.read_all')}}">/mensagens</a>''')

if __name__ == '__main__':
    app.run()