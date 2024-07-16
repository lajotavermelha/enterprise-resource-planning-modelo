from main import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    valor =db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Produto {self.nome}>'
   
'''
class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    funcionario = db.Column(db.String(100), nullable=False)
    produto = db.Column(db.String(100), nullable=False)
    valor_produto = db.Column(db.Integer, nullable=False)
    valor_total = db.Column(db.Integer, nullable=False)
''' 

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    salario = db.Column(db.Integer, nullable=False)
    