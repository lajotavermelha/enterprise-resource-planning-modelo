document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname === '/vendedor') {
        fetchVendas(), fetchProduto(), fetchVendedor()
    }
})


function fetchVendas() {
    fetch('/api/vendedor')
    .then(response => response.json())
    .then (data => {
        const vendasList = document.getElementById('vendas-body')
        vendasList.innerHTML = ''
        data.forEach(venda => {
            const row = document.createElement('tr')
            row.className = 'venda-item'
            row.innerHTML = `
                <td>${venda.id}</td>
                <td>${venda.funcionario.nome}</td>
                <td>${venda.produto.nome}</td>
                <td>${venda.quantidade}</td>
                <td>R$ ${venda.valor_produto.toFixed(2)}</td>
                <td>R$ ${venda.valor_total.toFixed(2)}</td>

            `
            vendasList.appendChild(row)
        })
        
    })
    .catch(error => console.error('Error fetching vendas:', error))
}

function fetchVendedor() {
    fetch('/api/recursoshumanos')
    .then( response => response.json())
    .then(data => {
        const vendedorList = document.getElementById('vendedor-list')
        vendedorList.innerHTML = ''
        data.forEach(funcionario => {
            const vendedorOption = document.createElement('option')
            vendedorOption.value = funcionario.id
            vendedorOption.text = funcionario.nome
            vendedorList.appendChild(vendedorOption)
        })
    })
    .catch(error => console.error('Error fetching products:', error));
}
function fetchProduto() {
    fetch('/api/estoque')
    .then(response => response.json())
    .then(data => {
        const produtoList = document.getElementById('produto-list');
        produtoList.innerHTML = '';
        data.forEach(produto => {
            const produtoOption = document.createElement('option');
            produtoOption.value = produto.id;
            produtoOption.text = `${produto.nome} (${produto.quantidade})`;
            produtoList.appendChild(produtoOption);
        });
        const calculateTotal = () => {
            const selectedProdutoId = produtoList.value;
            const selectedProduto = data.find(p => p.id == selectedProdutoId);

            if (selectedProduto) {
                const produtoValue = parseFloat(selectedProduto.valor);
                const quantidade = parseInt(document.getElementById('quantidade').value) || 0;
                const valor_produto = document.getElementById('valor_produto');
                const valor_total = document.getElementById('valor_total');

                valor_produto.textContent = `R$ ${produtoValue.toFixed(2)}`;
                valor_total.textContent = `R$ ${(produtoValue * quantidade).toFixed(2)}`;
            }
        };
        produtoList.addEventListener('change', calculateTotal);
        document.getElementById('quantidade').addEventListener('input', calculateTotal);
    })
    .catch(error => console.error('Error fetching products:', error));
}

function addVenda() {
    const funcionario_id = parseInt(document.getElementById('vendedor-list').value)
    const produto_id = parseInt(document.getElementById('produto-list').value)
    const quantidade= parseInt(document.getElementById('quantidade').value);
    const valorProdutoStr = document.getElementById('valor_produto').textContent;
    const valorTotalStr = document.getElementById('valor_total').textContent;
    const valorProduto = parseInt(valorProdutoStr.replace('R$ ', '').trim());
    const valorTotal = parseInt(valorTotalStr.replace('R$', '').trim())
    fetch('/api/vendedor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            funcionario_id: funcionario_id,
            produto_id: produto_id,
            quantidade: quantidade,
            valor_produto: valorProduto,
            valor_total: valorTotal
        })
    })
    
    .then(response => response.json())
    .then(() => {
        document.getElementById('quantidade').value = '';
        document.getElementById('valor_produto').value = '';
        document.getElementById('valor_total').value = '';
        fetchVendas();
        fetchProduto()
    })
    .catch(error => console.error('Error adding venda:', error));
    }

function editVenda(id) {
    const new_funcionario = prompt('Digite o nome do FUNCIONARIO:')
    const new_produto = prompt('Digite o nome do PRODUTO:')
    const new_quantidade = prompt('Digite a QUANTIDADE:')
    fetch(`/api/vendedor/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({funcionario: new_funcionario, produto: new_produto, quantidade: new_quantidade })
    })
    .then(response => response.json())
    .then(() => fetchVendas())
    .catch(error => console.error('Error updating venda:', error))
}

document.getElementById('logout-button').addEventListener('click', logout)

function logout(){
    fetch('/logout', {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => response.redirected)
    .then(() => window.location.href ='/login');
}