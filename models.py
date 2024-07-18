from db import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    valor =db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome}
   

class Vendas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=False)
    funcionario = db.relationship('Funcionario', backref=db.backref('vendas_funcionario', lazy=True))
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    produto = db.relationship('Produto', backref=db.backref('vendas_produtos', lazy=True))
    quantidade = db.Column(db.Integer, nullable=False)
    valor_produto = db.Column(db.Integer, nullable=False)
    valor_total = db.Column(db.Integer, nullable=False)


class Funcionario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    salario = db.Column(db.Integer, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome}
    