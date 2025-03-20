document.addEventListener('DOMContentLoaded', function() {
    const formSuino = document.getElementById('form-suino');
    
    if(formSuino) {
        formSuino.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const dados = {
                raca: this.raca.value,
                data_nascimento: this.data_nascimento.value,
                peso: this.peso.value,
                sexo: this.sexo.value
            };
            
            fetch('/api/adicionar_suino', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dados)
            })
            .then(response => response.json())
            .then(data => {
                if(data.success) {
                    alert('Suíno adicionado com sucesso!');
                    location.reload();
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                alert('Erro ao adicionar suíno');
            });
        });
    }
});

function editarSuino(id) {
    // Implementar edição
    console.log('Editar suíno:', id);
}

function deletarSuino(id) {
    // Implementar deleção
    console.log('Deletar suíno:', id);
}
