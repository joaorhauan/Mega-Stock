from flask import Blueprint, render_template, request
from app.models.Produto import Produto

bp_produto = Blueprint("produto",__name__)

@bp_produto.route("/")
def listar_produtos():
    produtos = Produto.query.all()
    return produtos

@bp_produto.route("/create", methods=['GET','POST'])
def criar_produto():
    if request.method == 'GET':
        # render_template('produto_create.html')
        return "formulario pra cadastrar produto"
    elif request.method == 'POST':
        # create product
        return "produto criado com sucesso"
    
@bp_produto.route("/update", methods=['GET','POST'])
def editar_produto():
    if request.method == 'GET':
        # render_template('produto_create.html')
        return "formulario pra atualizar produto"
    elif request.method == 'POST':
        # create product
        return "produto atualizado com sucesso"