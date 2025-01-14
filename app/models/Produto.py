from config import db

class Produto(db.Model):
    __tablename__="produto"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(100))
    preco = db.Column(db.Float)
    quantidade_estoque = db.Column(db.Integer)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    id_fornecedor = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=False)
    id_movestoque = db.Column(db.Integer, db.ForeignKey('movestoque.id'), nullable=False)
    

    categoria = db.relationship('Categoria', backref='produtos')
    fornecedor = db.relationship('Fornecedor', backref='produtos')
    moviestoque = db.relationship('MovEstoque', backref='produtos')


    def __init__(self, nome, descricao, preco, quantdade_estoque):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantdade_estoque = quantdade_estoque

    def __repr__(self):
        return "<Produto: {} - {} - {} - {} - {} - {}".format(self.produto.nome, self.produto.descricao, self.produto.preco, self.produto.quantidade_estoque, self.categoria.nome, self.fornecedor.nome)