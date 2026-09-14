

<!-- controle de estoque e outra aba (pag?!) controle de finanças-->
 2 <!-- TODO1: CADASTRAR PRODUTOS, REMOVER PRODUTOS (TALVEZ ATT), LISTAR PRODUTOS-->
 3 <!-- TODO2: ver saldo (talvez tbm receita completa), inserir movimentação

# como deve funcionar
- 2 funcionalidades: controle de estoque e gerenciar fluxo de caixa

- 1: cadastrar, atualizar e deletar produtos no estoque
- 2: operações de fluxo de caixa: inserir dinheiro q entra e sai nas vendas, e então poder listar as operações feitas

- 3: pagina inicial ser a listagem de estoque e ter botao pra abrir a pagina de finanças, na de finanças ter botao pra ir para a de estoque

# tarefas:
## 1
() criar funcionalidade de cadastro de produto no banco
    -se for add produto q ja existe, só incrementar qtd?

() criar html/form de cadastro

() criar funcionalidade de deletar produto no banco (por meio do id; o id sera mostrado na listagem do estoque pra facilitar)
() criar html/form de deleção de produto (baseado no id q aparecerá na listagem)

() criar listagem de produtos (+html); id do produto no banco deve aparecer (p/ ser usado em att e del)

() criar funcionalidade para remover qtd x de produto
    -baseado no id
    -se qtd_req > qtd_banco nao realizar e indicar q é maior

() esvaziar banco apos testes
() criar autenticacao simples?

## 2
>sobre o controle de operações de caixa
() criar func para listar todas as operações feitas (poder separar por dia?)
() func p/ registrar venda (registra valor da venda)
() listar valor total de todas vendas (no dia?)

() verificar se condiz com oq propus nos campos docx
() aperfeiçoar aparencia

# tarefas old
    -(X)add produto ao estoque
        (IMPL) o certo seria verificar se ja existe produto com esse nome e incrementar qtd?
    -remover qtx x (e/ou aoagar ao chegar em 0)
        -apenaa remover(ex: jogar prod. fora)
        -remover e movimentar caixa (ex: cliente comprou)

    -registrar fluxo de caixa
        -dinheiro q sai/entra; "vender produto" é feiro via "remover produto"(func ali acima)

    -listar estoque (talvez limitar por 100 produtos..)
         -talvez ter opcao pra buscar produto (filtro? por nome e/ou por valor?? e ou por qtd?)




# old
obs: e se for inserir + de 1 prod, seria melhor ter vtn pra limpar campo, mas salvar dados, entao enviar tudo numa lista com btn "confurmar (x) produtos"
# cs
- prineiro so fazer crud funcional
- dps add authentication
- e/ou outras techs...

