from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.Categoria import Categoria
from config import db

bp_categoria = Blueprint("categoria",__name__)

@bp_categoria.route("/")
def listar_categorias():
    categorias = Categoria.query.all()
    return render_template('categorias.html', categorias=categorias)

@bp_categoria.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('criar_categoria.html')
    elif request.method == 'POST':
        
        nome = request.form['nome']
        descricao = request.form['descricao']
        
        categoria = Categoria(nome,descricao)

        db.session.add(categoria)
        db.session.commit()

        return redirect(url_for('categoria.listar_categorias'))
    
@bp_categoria.route("/update/<id>", methods=['GET','POST'])
def update(id):
    if request.method == 'GET':
        return render_template('editar_categoria.html')
    elif request.method == 'POST':

        return "categoria atualizada com sucesso"
    

@bp_categoria.route("/delete/<id>", methods=['POST'])
def delete(id):
    categoria = Categoria.query.filter_by(id)
    db.session.delete(categoria)
    db.session.commit()
    return "deletado com sucesso papae"