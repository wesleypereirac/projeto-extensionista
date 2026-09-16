
function retirarQtd(nome, qtdAtual) {
    qtdAtual = parseInt(qtdAtual);
    const qtd = prompt(`Quantidade atual: ${qtdAtual}\nQuanto deseja retirar?`);

    if (qtd === null) return; // cancelou

    const qtdNum = parseInt(qtd);

    if (isNaN(qtdNum) || qtdNum <= 0) {
        alert("Digite uma quantidade válida.");
        return;
    }

    if (qtdNum > qtdAtual) {
        alert("Não é possível retirar mais do que a quantidade em estoque.");
        return;
    }

    // Envia para o backend
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/retirar';

    const inputNome = document.createElement('input');
    inputNome.type = 'hidden';
    inputNome.name = 'nome';
    inputNome.value = nome;

    const inputQtd = document.createElement('input');
    inputQtd.type = 'hidden';
    inputQtd.name = 'qtd';
    inputQtd.value = qtdNum;

    form.appendChild(inputNome);
    form.appendChild(inputQtd);
    document.body.appendChild(form);
    form.submit();
}

function abrirEdicao(id) {
    document.getElementById('form-' + id).style.display = 'block';
}

function fecharEdicao(id) {
    document.getElementById('form-' + id).style.display = 'none';
}

function confirmarDelete(id, nome) {
    const confirmou = confirm(`Tem certeza que deseja excluir o produto "${nome}"?`);

    if (confirmou) {
        // Cria um formulário temporário e envia
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = '/deletar';

        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'id';
        input.value = id;

        form.appendChild(input);
        document.body.appendChild(form);
        form.submit();
    }
}