document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname === '/recursoshumanos'){
        fetchFuncionarios();
    }

});

function fetchFuncionarios() {
    fetch('/api/recursoshumanos')
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
                    <button onclick="editFuncionario(${funcionario.id})">Editar</button>
                    <button onclick="deleteFuncionario(${funcionario.id})">Excluir</button>
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

    fetch('/api/recursoshumanos',  {
        method:'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nome: nome_funcionario, salario: salario_funcionario})
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById('nome-funcionario').value = ''
        document.getElementById('salario-funcionario').value = ''
        fetchFuncionarios()
    })
    .catch(error => console.error('Error adding product:', error));
}

function editFuncionario(id) {
    const new_nome_funcionario = prompt('Digite o novo NOME do Funcionario: ')
    const new_salario_funcionario = prompt('Digite o novo SALARIO do funcionario: ')

    fetch(`/api/recursoshumanos/${id}`,  {
        method:'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nome: new_nome_funcionario, salario: new_salario_funcionario})
    })
    .then(response => response.json())
    .then(() => fetchFuncionarios())
    .catch(error => console.error('Error adding product:', error));
}

function deleteFuncionario(id) {
    fetch(`/api/recursoshumanos/${id}`,  {
        method:'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => response.json())
    .then(() => fetchFuncionarios())
    .catch(error => console.error('Error adding product:', error));
}