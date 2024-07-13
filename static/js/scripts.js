document.addEventListener('DOMContentLoaded', () => {
    fetchProducts();
});

function fetchProducts() {
    fetch('/produtos')
        .then(response => response.json())
        .then(data => {
            const productList = document.getElementById('product-list')
            productList.innerHTML = ''
            data.forEach(product => {
                const productItem = document.createElement('div')
                productItem.className = 'product-item'
                productItem.innerHTML= `
                    <span>${product.nome} (${product.quantidade})</span>
                    <div>
                        <button onclick="editProduct(${product.id})">Editar</button>
                        <button onclick="deleteProduct(${product.id})">Deletar</button>
                    </div>
                `;
                productList.appendChild(productItem)
            })

        })
}

function addProduct() {
    const name = document.getElementById('product-name').value 
    const quantity = document.getElementById('product-quantity').value

    fetch('/produtos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nome: name, quantidade: quantity})
    })
    .then(response => response.JSON())
    .then(() => {
        document.getElementById('product-name').value = '';
        document.getElementById('product-quantity').value = '';
        fetchProducts();
    })
}

function editProduct(id) {
    const newName = prompt('Digite o novo nome do produto: ')
    const newQuantity = prompt('Digite a quantidade do produto: ')

    fetch(`/produtos/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nome: newName, quantidade: newQuantity})
    })
    .then(response => response.json())
    .then(() => fetchProducts())
}

function deleteProduct(id) {
    fetch(`/produtos/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(() => fetchProducts())
}