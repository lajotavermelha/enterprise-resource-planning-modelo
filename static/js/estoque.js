document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname === '/estoque'){
        fetchProducts();
    }

});

function fetchProducts() {
    fetch('/api/estoque')
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

    fetch('/api/estoque', {
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

    fetch(`/api/estoque/${id}`, {
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
    fetch(`/api/estoque/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(() => fetchProducts())
    .catch(error => console.error('Error deleting product:', error));
}