from datetime import datetime
from config import db

class MovEstoque(db.Model):
    __tablename__ = "movestoque"

    id = db.Column(db.Integer, primary_key=True)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id', ondelete='CASCADE'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    observacao = db.Column(db.String(200))

    # Relacionamento com Produto
    produto = db.relationship('Produto', back_populates='movestoque')
