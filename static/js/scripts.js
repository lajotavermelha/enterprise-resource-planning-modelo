document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname === '/produtos-page'){
        fetchProducts();
    }
});

function fetchProducts() {
    fetch('/produtos')
        .then(response => response.json())
        .then(data => {
            const productList = document.getElementById('product-list');
            productList.innerHTML = '';
            data.forEach(product => {
                const productItem = document.createElement('div');
                productItem.className = 'product-item';
                productItem.innerHTML = `
                    <span>${product.nome} (${product.quantidade}) R$${product.valor}</span>
                    <div>
                        <button onclick="editProduct(${product.id})">Editar</button>
                        <button onclick="deleteProduct(${product.id})">Excluir</button>
                    </div>
                `;
                productList.appendChild(productItem);
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}

function addProduct() {
    const name = document.getElementById('product-name').value;
    const quantity = document.getElementById('product-quantity').value;
    const value = document.getElementById('product-value').value

    fetch('/produtos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome: name, quantidade: quantity, valor:value })
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById('product-name').value = '';
        document.getElementById('product-quantity').value = '';
        document.getElementById('product-value').value = '';
        fetchProducts();
    })
    .catch(error => console.error('Error adding product:', error));
}

function editProduct(id) {
    const newName = prompt('Digite o novo NOME do produto: ');
    const newQuantity = prompt('Digite a nova QUANTIDADE do produto: ');
    const newValue = prompt('Digite o novo VALOR do produto: ');

    fetch(`/produtos/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome: newName, quantidade: newQuantity, valor: newValue })
    })
    .then(response => response.json())
    .then(() => fetchProducts())
    .catch(error => console.error('Error editing product:', error));
}

function deleteProduct(id) {
    fetch(`/produtos/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(() => fetchProducts())
    .catch(error => console.error('Error deleting product:', error));
}

function fetchFuncionarios() {
    fetch('/recursoshumanos')
    .then( response => response.json())
    .then(data => {
        const funcionariosList = document.getElementById('funcionarios-list')
        funcionariosList.innerHTML = ''
        data.forEach(funcionario => {
            const funcionariosItem = document.createElement('div')
            funcionariosItem.className = 'funcionario-item'
            funcionariosItem.innerHTML = `
                <span>${funcionario.nome} R$${funcionario.salario}</span>
                <div>
                    <button onclick="editProduct(${funcionario.id})">Editar</button>
                    <button onclick="deleteProduct(${funcionario.id})">Excluir</button>
                </div>
            `
            funcionariosList.appendChild(funcionariosItem)
        })
    })
    .catch(error => console.error('Error fetching products:', error));
}
function addFuncionario() {
    const nome_funcionario = document.getElementById('nome-funcionario').value
    const salario_funcionario = document.getElementById('salario-funcionario').value

    fetch('/recursoshumanos',  {
        method:'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nome: nome_funcionario, salario: salario_funcionario})
    })
    .then(() => {
        document.getElementById('nome-funcionario').value = ''
        document.getElementById('salario-funcionario').value = ''
        fetchFuncionarios()
    })
    .catch(error => console.error('Error adding product:', error));
}

