from datetime import datetime
from config import db

class MovEstoque(db.Model):
    __tablename__ = "movestoque"


    id = db.Column(db.Integer, primary_key = True)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable = False)
    tipo = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    observacao = db.Column(db.String(200))

    def __init__(self, tipo, quantidade, data_hora, observacao):
        self.tipo = tipo
        self.quantidade = quantidade
        self.data_hora = data_hora
        self.observacao = observacao