from flask import request, jsonify
from main import app, db
from models import Produto

@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([{
        'nome': produto.nome,
        'quantidade': produto.quantidade
    } for produto in produtos])

@app.route('/produtos', methods=['POST'])
def add_produto():
    data = request.get_json()
    novo_produto = Produto(nome=data['nome'], quantidade=data['quantidade'])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'message': 'Produto adicionado'}), 201

@app.route('/produtos/<int:id>', methods=['PUT'])
def update_produto(id):
    data = request.get_json()
    produto = Produto.query.get_or_404(id)
    produto.nome = data.get('nome', produto.nome)
    produto.quantidade = data.get('quantidade', produto.quantidade)
    db.session.commit()
    return jsonify({'message': 'Produto atualizado'})

@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'message': 'Produto deletado'})

@app.route('/produtos/<int:id>', methods=['GET'])
def get_produto(id):
    produto = Produto.query.get_or_404(id)
    return jsonify({
        'nome': produto.nome,
        'quantidade': produto.quantidade
    })
