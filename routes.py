from flask import request, jsonify, render_template
from main import app, db
from models import Produto, Funcionario, Vendas


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/estoque')
def produtos_page():
    return render_template('produtos.html')
@app.route('/recursoshumanos')
def recursos_humanos():
    return render_template('recursoshumanos.html')

@app.route('/api/estoque', methods=['GET', 'POST'])
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

@app.route('/api/estoque/<int:id>', methods=['PUT', 'DELETE'])
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
    
@app.route('/api/recursoshumanos', methods=['GET', 'POST'])
def manage_funcionarios():
    if request.method == 'GET':
        funcionarios = Funcionario.query.all()
        return jsonify([{'id': f.id, 'nome': f.nome, 'salario': f.salario} for f in funcionarios])
    elif request.method == 'POST':
        data = request.get_json()
        novo_funcionario = Funcionario(nome=data['nome'], salario=data['salario'])
        db.session.add(novo_funcionario)
        db.session.commit()
        return jsonify({'message': 'funcionario criado'}), 201

@app.route('/api/recursoshumanos/<int:id>', methods=['PUT', 'DELETE'])
def update_delete_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    if request.method == 'PUT':
        data = request.get_json()
        funcionario.nome = data['nome']
        funcionario.salario = data['salario']
        db.session.commit()
        return jsonify({'message': 'funcionario atualizado'}), 200
    elif request.method == 'DELETE':
        db.session.delete(funcionario)
        db.session.commit()
        return jsonify({'message': 'funcionario deletado'}), 200
            
@app.route('/api/vendas', methods=['GET', 'POST'])
def get_add_vendas():
    if request.method == 'GET':
        vendas = Vendas.query.all()
        return jsonify([{'id': v.id,
                         'funcionario': v.funcionario,
                         'produto': v.produto,
                         'quantidade': v.quantidade,
                         'valor_produto': v.valor_produto,
                         'valor_total': v.valor_total
                         }]for v in vendas)
    elif request.method == 'POST':
        data = request.get_json()
        nova_venda = Vendas(
            funcionario = data['funcionario'],
            produto = data['produto'],
            quantidade = data['quantidade'],
            valor_produto = data['valor_produto'],
            valor_total = data['valor_total']
        )
        db.session.add(nova_venda)
        db.session.commit()
        return jsonify({'message': 'venda concliuda'}), 201
    
@app.route('/api/vendas/<int:id>', methods=['PUT'])
def delete_vendas(id):
    venda = Vendas.query.get_or_404(id)
    if request.method == 'PUT':
        data = request.get_json()
        venda.data = request.get_json()
        venda.funcionario = data['funcionario'],
        venda.produto = data['produto'],
        venda.quantidade = data['quantidade'],
        venda.valor_produto = data['valor_produto'],
        venda.valor_total = data['valor_total']
        db.session.commit()
        return jsonify({'message': 'venda editada'})