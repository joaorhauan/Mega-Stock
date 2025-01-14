from config import db

class Fornecedor(db.Model):
    __tablename__ = "fornecedor"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    contato = db.Column(db.String(100))
    endereco = db.Column(db.String(200))


    def __init__(self,nome,contato,endereco):
        self.nome = nome
        self.contato = contato
        self.endereco = endereco