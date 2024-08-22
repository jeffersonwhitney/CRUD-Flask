from flask import Flask, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from database import db
from usuarios import bp_usuarios 

app = Flask(__name__)

conexao = "sqlite:///meubanco.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao

db.init_app(app)
app.config['SECRET_KEY'] = 'secret'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

migrate = Migrate(app, db)

app.register_blueprint(bp_usuarios, url_prefix='/usuarios', name='bp_usuarios') 

@app.route('/')
def index():
    create_link = url_for('bp_usuarios.create') 
    read_link = url_for('bp_usuarios.read')    

    return f"""
    Seja bem vindo ao Programa listador de livros! <br>
    <a href="{create_link}">Adicionar livro</a><br>
    <a href="{read_link}">Listar livros</a><br>
    """

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)