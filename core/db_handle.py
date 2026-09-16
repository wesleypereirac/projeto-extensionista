import sqlite3

#retorna conexão com o banco para poder ser manipulado
def get_db_handlrs():
    con = sqlite3.connect('data/data.db')
    cur = con.cursor()
    
    cur.execute('create table if not exists produtos(pk INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, valor DECIMAL, qtd INTEGER)')
    con.commit()

    cur.execute('create table if not exists fluxo_caixa(pk INTEGER PRIMARY KEY AUTOINCREMENT, valor DECIMAL, data_hora_operacao TEXT)')
    con.commit()
    return cur,con

#operacoes de estoque
def db_insert_or_update_qtd(tabela, valores: tuple):
    """
    valores = (nome, valor, qtd)
    Se já existir produto com o mesmo nome → soma a quantidade
    Se não existir → insere novo
    """
    cur, con = get_db_handlrs()
    if tabela == 'produtos':
        nome, valor, qtd = valores

        # Verifica se já existe para apenas incrementar a qtd na mesma
        cur.execute(f'SELECT pk, qtd FROM {tabela} WHERE nome = ?', (nome,))
        resultado = cur.fetchone()

        if resultado:
            # Já existe → atualiza a quantidade
            id_existente, qtd_atual = resultado
            nova_qtd = qtd_atual + int(qtd)

            cur.execute(
                f'UPDATE {tabela} SET qtd = ?, valor = ? WHERE pk = ?',
                (nova_qtd, valor, id_existente)
            )
            con.commit()
            

        else:
            cur.execute(
                    f'INSERT INTO {tabela} (nome, valor, qtd) VALUES (?, ?, ?)',
                    (nome, valor, qtd)
                )
            con.commit()

    elif tabela == 'fluxo_caixa':
        cur.execute(
            f"INSERT INTO {tabela} (valor, data_hora_operacao) VALUES (?, datetime('now', 'localtime'))",
            (valores[0]) #valor
            )
        
        con.commit()

#consultar
def db_query(elemnt,tabela,condicao=''):
    cur,con = get_db_handlrs()
    res = cur.execute(f'select {elemnt} from {tabela} {condicao}')
    return res.fetchall()

#atualizar
def db_update(tabela, id_produto, valores: tuple):
    cur, con = get_db_handlrs()
    # valores = (nome, valor, qtd)
    cur.execute(
        f'UPDATE {tabela} SET nome = ?, valor = ?, qtd = ? WHERE pk = ?',
        (*valores, id_produto)
    )
    con.commit()

#deletar
def db_delete(tabela, id_produto):
    cur, con = get_db_handlrs()
    cur.execute(f'DELETE FROM {tabela} WHERE pk = ?', (id_produto,))
    con.commit()

#remover qtd
def remover_qtd(tabela, nome, qtd_retirar):
    cur, con = get_db_handlrs()

    # Busca a quantidade atual pela PK (nome)
    cur.execute(f'SELECT qtd FROM {tabela} WHERE nome = ?', (nome,))
    resultado = cur.fetchone()

    if not resultado:
        return False  # produto não encontrado

    qtd_atual = resultado[0]

    if qtd_retirar > qtd_atual:
        return False  # tentou tirar mais do que tem

    nova_qtd = qtd_atual - qtd_retirar

    cur.execute(
        f'UPDATE {tabela} SET qtd = ? WHERE nome = ?',
        (nova_qtd, nome)
    )
    con.commit()
    return True

#operacoes de finanças
