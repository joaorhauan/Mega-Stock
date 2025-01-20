from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.Fornecedor import Fornecedor
from config import db

bp_fornecedores = Blueprint("fornecedores",__name__)

@bp_fornecedores.route("/")
def listar_fornecedores():
    fornecedores = Fornecedor.query.all()
    return render_template('fornecedores.html', fornecedores=fornecedores)

@bp_fornecedores.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('criar_fornecedor.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        contato = request.form['contato']
        endereco = request.form['endereco']


        fornecedor = Fornecedor(nome,contato,endereco)

        db.session.add(fornecedor)
        db.session.commit()

        return redirect(url_for('fornecedores.listar_fornecedores'))


