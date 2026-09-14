import sqlite3

def get_db_handlrs():
    con = sqlite3.connect('data/data.db')
    cur = con.cursor()
    #remover linha abaixo
    cur.execute('create table if not exists produtos(pk INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, valor DECIMAL, qtd INTEGER)')
    #remover isso acima apos criar
    con.commit()
    return cur,con

def db_insert(tabela, valores: tuple):
    cur,con = get_db_handlrs()
    cur.execute(f'insert into {tabela} (nome, valor, qtd) values (?,?,?)', valores)
    con.commit()

def db_query(elemnt,tabela,condicao=''):
    cur,con = get_db_handlrs()
    res = cur.execute(f'select {elemnt} from {tabela} {condicao}')
    return res.fetchall()

def db_update():
    pass