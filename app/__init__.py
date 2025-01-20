import os
from flask import Flask
from flask_migrate import Migrate
from config import db
from .routes.produto import bp_produto
from .routes.categoria import bp_categoria
from .routes.fornecedores import bp_fornecedores

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
        from app.models.Produto import Produto
        from app.models.MovimentacaoEstoque import MovEstoque
        from app.models.Categoria import Categoria
        from app.models.Fornecedor import Fornecedor
        db.create_all()

    app.register_blueprint(bp_produto, url_prefix="/produtos")
    app.register_blueprint(bp_categoria, url_prefix="/categorias")
    app.register_blueprint(bp_fornecedores, url_prefix="/fornecedores")

    return app