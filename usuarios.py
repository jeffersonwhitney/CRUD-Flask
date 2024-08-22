import os

from flask import Blueprint, current_app, redirect, request
from flask.templating import render_template
from werkzeug.utils import secure_filename

from database import db
from models import Usuario

bp_usuarios = Blueprint("usuarios", __name__, template_folder="templates")

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('usuarios_create.html')

    if request.method == 'POST':
        nome = request.form.get('nome')
        arquivo_pdf = request.files['pdf_file']
        uploads_dir = os.path.join(os.path.dirname(__file__), '..', 'static', 'uploads')
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        if arquivo_pdf and allowed_file(arquivo_pdf.filename):
            if arquivo_pdf.filename:
                filename = secure_filename(arquivo_pdf.filename)
                arquivo_pdf.save(
                  os.path.join(
                    bp_usuarios.root_path, '..', 
                    current_app.config['UPLOAD_FOLDER'], filename))
                u = Usuario(nome, filename)
                db.session.add(u)
                db.session.commit()
                return 'Livro cadastrado com sucesso!'
            else:
                return 'Erro: Nenhum arquivo selecionado.'
        else:
            return 'Erro no upload do arquivo. Certifique-se de enviar um arquivo PDF válido.'

    return 'Erro'

@bp_usuarios.route('/read')
def read():
  lista_usuarios = Usuario.query.all()
  return render_template('usuarios_read.html', usuarios=lista_usuarios)
  
@bp_usuarios.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  if request.method=='GET':
    u = Usuario.query.get(id)
    if u is None:
      return "Livro não encontrado" 
    return render_template('usuarios_update.html', u = u)
  if request.method=='POST':
    nome = request.form.get('nome')
    u = Usuario.query.get(id)
    if u is not None: 
      u.nome = nome
      db.session.add(u)
      db.session.commit()
      return redirect('/usuarios/read')
    else:
      return "Livro não encontrado"
  return 'Erro'

@bp_usuarios.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  if request.method=='GET':
    u = Usuario.query.get(id)
    return render_template('usuarios_delete.html', u = u)
  if request.method=='POST':
    u = Usuario.query.get(id)
    db.session.delete(u)
    db.session.commit()  
    return 'Dados excluidos com sucesso'
  return 'Erro'
  