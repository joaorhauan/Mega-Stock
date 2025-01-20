from flask import Blueprint, render_template, request, flash
from app.models.Produto import Produto
from app.models.Categoria import Categoria
from app.models.Fornecedor import Fornecedor
from config import db

bp_produto = Blueprint("produto",__name__)

@bp_produto.route("/")
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos)

@bp_produto.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('criar_produto.html')
    elif request.method == 'POST':
        

        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        quantidade_estoque = request.form['quantidade_estoque']
        categoria = request.form['categoria']
        fornecedor = request.form['fornecedor']

        id_categoria = Categoria.query.filter_by(nome=categoria).first()
        id_fornecedor = Fornecedor.query.filter_by(nome=fornecedor).first()

        print(id_categoria)
        
        produto = Produto(nome,descricao,preco,quantidade_estoque, id_categoria.id, id_fornecedor.id)


        db.session.add(produto)
        db.session.commit()


        return "produto criado com sucesso"
    
@bp_produto.route("/update/<id>", methods=['GET','POST'])
def update(id):
    if request.method == 'GET':
        return render_template('editar_produto.html')
    elif request.method == 'POST':

        return "produto atualizado com sucesso"
    

@bp_produto.route("/delete/<id>", methods=['POST'])
def delete(id):
    produto = Produto.query.filter_by(id)
    db.session.delete(produto)
    db.session.commit()
    return "deletado com sucesso papae"