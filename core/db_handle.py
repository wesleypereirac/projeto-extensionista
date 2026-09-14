import sqlite3

#retorna conexão com o banco para poder ser manipulado
def get_db_handlrs():
    con = sqlite3.connect('data/data.db')
    cur = con.cursor()
    #remover linha abaixo
    cur.execute('create table if not exists produtos(pk INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, valor DECIMAL, qtd INTEGER)')
    con.commit()
    return cur,con

#cadastrar ou incrementar qtd
def db_insert_or_update_qtd(tabela, valores: tuple):
    """
    valores = (nome, valor, qtd)
    Se já existir produto com o mesmo nome → soma a quantidade
    Se não existir → insere novo
    """
    cur, con = get_db_handlrs()
    nome, valor, qtd = valores

    # Verifica se já existe
    cur.execute(f'SELECT pk, qtd FROM {tabela} WHERE nome = ?', (nome,))
    resultado = cur.fetchone()

    if resultado and tabela == 'produtos':
        # Já existe → atualiza a quantidade
        id_existente, qtd_atual = resultado
        nova_qtd = qtd_atual + int(qtd)

        cur.execute(
            f'UPDATE {tabela} SET qtd = ?, valor = ? WHERE pk = ?',
            (nova_qtd, valor, id_existente)
        )
    else:
        # Não existe → insere novo
        cur.execute(
            f'INSERT INTO {tabela} (nome, valor, qtd) VALUES (?, ?, ?)',
            (nome, valor, qtd)
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