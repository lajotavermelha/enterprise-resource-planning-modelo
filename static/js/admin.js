document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname === '/vendedor') {
        fetchVendas()
    }
})

function fetchVendas() {
    fetch('/api/vendedor')
    .then(response => response.json())
    .then (data => {
        console.log(data)
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