from database import db


class Usuario(db.Model):
  __tablename__ = "usuario"
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  caminho_pdf = db.Column(db.String(200))
  
  def __init__(self, nome, caminho_pdf):
    self.nome = nome
    self.caminho_pdf = caminho_pdf
    
  def __repr__(self):
    return f"Usuario('{self.nome}', '{self.caminho_pdf}')"