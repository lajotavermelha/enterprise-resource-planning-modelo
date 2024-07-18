from flask import request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from main import app, db
from models import Produto, Funcionario, Vendas

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        password = request.form['password']
        user = Funcionario.query.filter_by(nome=nome).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('vendedor'))
        else:
            flash('Usuário ou senha inválidos')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('login'))

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        return redirect(url_for('vendedor'))
    return render_template('admin.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/estoque')
def produtos_page():
    return render_template('produtos.html')
@app.route('/recursoshumanos')
def recursos_humanos():
    return render_template('recursoshumanos.html')

@app.route('/vendas')
def vendas():
    return render_template('vendas.html')

@app.route('/vendedor')
@login_required
def vendedor():
    return render_template('vendedor.html', user=current_user)

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
        novo_funcionario = Funcionario(nome=data['nome'], salario=data['salario'], password_hash=generate_password_hash(data['password']), is_admin=data['is_admin'])
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
            
@app.route('/api/vendedor', methods=['GET', 'POST'])
def get_add_vendas():
    if request.method == 'GET':
        if current_user.is_admin:
            vendas = Vendas.query.all()
        else:
            vendas = Vendas.query.filter_by(funcionario_id=current_user.id).all()
        return jsonify([{'id': v.id,
                         'funcionario': v.funcionario.to_dict(),
                         'funcionario_id': v.funcionario_id,
                         'produto': v.produto.to_dict(),
                         'produto_id': v.produto_id,
                         'quantidade': v.quantidade,
                         'valor_produto': v.valor_produto,
                         'valor_total': v.valor_total
                         }for v in vendas])
    elif request.method == 'POST':
        data = request.get_json()
        nova_venda = Vendas(
            funcionario_id= current_user.id if not current_user.is_admin else data['funcionario_id'],
            produto_id=data['produto_id'],
            quantidade = data['quantidade'],
            valor_produto = data['valor_produto'],
            valor_total = data['valor_total']
        )
        db.session.add(nova_venda)
        db.session.commit()
        return jsonify({'message': 'venda concliuda'}), 201
    
@app.route('/api/vendedor/<int:id>', methods=['PUT'])
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