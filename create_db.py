from main import app, db
from models import Produto, Funcionario


with app.app_context():
    db.create_all()
    print("Banco de dados criado")