from config import db

class Categoria(db.Model):
    __tablename__="categoria"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(200))

    def __init__(self,nome,descricao):
        self.nome = nome
        self.descricao = descricao