from flask import request, jsonify, render_template
from main import app, db
from models import Produto, Funcionario


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/produtos-page')
def produtos_page():
    return render_template('produtos.html')
@app.route('/recursoshumanos')
def recursos_humanos():
    return render_template('recursoshumanos.html')

@app.route('/produtos', methods=['GET', 'POST'])
def manage_produtos():
    if request.method == 'GET':
        produtos = Produto.query.all()
        return jsonify([{'id': p.id, 'nome': p.nome, 'quantidade': p.quantidade, 'valor': p.valor} for p in produtos])
    elif request.method == 'POST':
        data = request.get_json()
        novo_produto = Produto(nome=data['nome'], quantidade=data['quantidade'], valor=data['valor'])
        db.session.add(novo_produto)
        db.session.commit()
        return jsonify({'message': 'Produto adicionado'}), 201

@app.route('/produtos/<int:id>', methods=['PUT', 'DELETE'])
def update_delete_produto(id):
    produto = Produto.query.get_or_404(id)
    if request.method == 'PUT':
        data = request.get_json()
        produto.nome = data['nome']
        produto.quantidade = data['quantidade']
        produto.valor = data['valor']
        db.session.commit()
        return jsonify({'message': 'Produto atualizado'}), 200
    elif request.method == 'DELETE':
        db.session.delete(produto)
        db.session.commit()
        return jsonify({'message': 'Produto excluído'}), 200
    
@app.route('/recursoshumanos', methods=['GET', 'POST'])
def manage_funcionario():
    if request.method == 'GET':
        funcionarios = Funcionario.query.all()
        return jsonify([{'id': f.id, 'nome': f.nome, 'salario': f.salario} for f in funcionarios])
    elif request.method == 'POST':
        data = request.get_json()
        novo_funcionario = Funcionario(nome=data['nome'], salario=data['salario'])
        db.session.add(novo_funcionario)
        db.session.commit()
        return jsonify({'message': 'funcionario criado'}), 201

@app.route('/recursoshumanos/<int:id>', methods=['PUT', 'DELETE'])
def update_delete_funcionario(id):
    if request.method == 'PUT':
        data = request.get_json()
        funcionario.nome = data['nome']
        funcionario.salario = data['salario']
        db.session.commit()
        return jsonify({'message': 'funcionario atualizado'}), 201
    elif request.method == 'DELETE':
        db.session.delete(funcionario)
        db.session.commit()
        return jsonify({'message': 'funcionario deletado'}), 201
            
