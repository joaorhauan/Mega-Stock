import os
from flask import Flask
from app.models import Produto, MovimentacaoEstoque, Fornecedor, Categoria
from flask_migrate import Migrate
from config import db


def create_app():
    app = Flask(__name__)

    app.config['SECRET KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    mydb = os.getenv('DB_DATABASE')

    conexao = f"mysql+pymysql://{username}:{password}@{host}/{mydb}"

    app.config['SQLALCHEMY_DATABASE_URI'] = conexao


    db.init_app(app)
    migrate = Migrate(app,db)
    migrate.init_app(app, db)

    with app.app_context():
        from . import models

    return app