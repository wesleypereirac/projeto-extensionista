function confirmarDelete(id, nome) {
    const confirmou = confirm(`Tem certeza que deseja excluir a venda?`);

    if (confirmou) {
        // Cria um formulário temporário e envia
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = '/deletar_venda';

        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'id';
        input.value = id;

        form.appendChild(input);
        document.body.appendChild(form);
        form.submit();
    }
}

//main

//requisitar filtro à api quando clicar na opcao do select
 const select_filtro_historico = document.querySelector("#filtro");

    select_filtro_historico.addEventListener("change", function() {
        this.form.submit();
    });

//filtro e renderiza informacao do valor total
const filtro = document.querySelector("#filtro_total_vendas");
const total = document.querySelector("#log_valor_vendas");

async function atualizarTotal() {
    const periodo = filtro.value;

    const response = await fetch(`/vendas?periodo=${periodo}`);
    const data = await response.json();

    total.textContent = `R$: ${data.total}`;
}

filtro.addEventListener("change", atualizarTotal);

//on dom load
document.addEventListener('DOMContentLoaded', function() {
   //verificar qual valor do span e entao alterar o select pra ele
    const select = document.querySelector("#filtro");
    const valorAnterior = document.querySelector("#filtro_atual").textContent.trim();

    select.value = valorAnterior;
  });

document.addEventListener("DOMContentLoaded", atualizarTotal);