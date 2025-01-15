from config import db

class Produto(db.Model):
    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    preco = db.Column(db.Float, nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id', ondelete='CASCADE'), nullable=False)
    id_fornecedor = db.Column(db.Integer, db.ForeignKey('fornecedor.id', ondelete='CASCADE'), nullable=False)

    # Relacionamentos
    categoria = db.relationship('Categoria', backref='produtos', lazy=True)
    fornecedor = db.relationship('Fornecedor', backref='produtos', lazy=True)
    movestoque = db.relationship('MovEstoque', back_populates='produto', lazy=True, foreign_keys='MovEstoque.id_produto')

    def __init__(self, nome, descricao, preco, quantidade_estoque, id_categoria, id_fornecedor):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.id_categoria = id_categoria
        self.id_fornecedor = id_fornecedor

    def __repr__(self):
        return f"<Produto: {self.nome} - {self.descricao} - R${self.preco:.2f} - Estoque: {self.quantidade_estoque}>"
