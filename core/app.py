import db_handle as db_handle
from flask import Flask, request, render_template, flash, redirect, url_for
import logging

app = Flask('app.py')
app.config["SECRET_KEY"] = "wlsec"

#BLOCO: estoque

##rendereizar estoque;
@app.route('/')
def index():
    return redirect(url_for('estoque')) 


#cadastr. produtos
#acho q teria q usar lib request e verificar se é post
@app.route('/cadastrar_produto',methods=["GET","POST"])
def cad():
    if request.method == "POST":
        nome = request.form.get('nome_produto')
        valor = request.form.get('valor_produto')
        qtd = request.form.get('qtd_produto')
    
        db_handle.db_insert_or_update_qtd('produtos',(nome,valor,qtd))

        #indicar sucesso
        flash("Produto cadastrado com sucesso!", "success") 
        return redirect(url_for("cad"))
    
    elif request.method.lower() == 'get':
        return render_template('cadastrar.html')
        

@app.route('/atualizar', methods=['POST'])
def atualizar():
    id_produto = request.form.get('id')
    nome = request.form.get('nome')
    valor = request.form.get('valor')
    qtd = request.form.get('qtd')

    db_handle.db_update('produtos', int(id_produto), (nome, valor, qtd))  # você adapta sua função

    flash("Produto atualizado com sucesso!", "success")
    return redirect(url_for('estoque'))


@app.route('/estoque')
def estoque():
    lista_dados = db_handle.db_query('*','produtos')

    return render_template('estoque.html',context=lista_dados)

@app.route('/deletar_produto', methods=['POST'])
def del_produto():
    id_produto = request.form.get('id')

    db_handle.db_delete('produtos', id_produto)

    flash("Produto excluído com sucesso!", "success")
    return redirect(url_for('estoque'))

#trata ratirar x qtd de produto
@app.route('/retirar', methods=['POST'])
def retirar():
    nome = request.form.get('nome')
    qtd = request.form.get('qtd')

    try:
        qtd = int(qtd)
    except (TypeError, ValueError):
        flash("Quantidade inválida.", "error")
        return redirect(url_for('estoque'))

    sucesso = db_handle.remover_qtd('produtos', nome, qtd)

    if sucesso:
        flash("Quantidade retirada com sucesso!", "success")
    else:
        flash("Não foi possível retirar a quantidade.", "error")

    return redirect(url_for('estoque'))


#BLOCO: finanças

##operacoes
@app.route('/registrar_venda', methods=['POST'])
def reg_venda():

    if request.method == "POST":
        valor = request.form.get('valor_venda')
        db_handle.db_insert_or_update_qtd('fluxo_caixa',(valor,))
        flash("Venda registrada com sucesso!", "success") 
        return redirect(url_for("list_vendas"))
    
    

@app.route('/listar_vendas',methods=['GET','POST'])
def list_vendas():
    filtro = request.form.get('filtro', 'last3days')
    periodo = None

    periodos = {
        'last3days': '-2 days',
        'last7days': '-6 days',
        'last30days': '-29 days',
        'last1year': '-1 year'
    }

    periodo = periodos.get(filtro)

    list_regs = db_handle.db_query(
        '*',
        'fluxo_caixa',
        f"""WHERE data_hora_operacao >= datetime('now', 'localtime', '{periodo}', 'start of day')
        AND data_hora_operacao <= datetime('now', 'localtime')"""
    )
    list_regs.append(filtro)
    return render_template('fluxo_vendas.html',context=list_regs)

##requisicoes das paginas
@app.route('/deletar_venda', methods=['POST'])
def del_venda():
    id_produto = request.form.get('id')

    db_handle.db_delete('fluxo_caixa', id_produto) 

    flash("Venda excluída com sucesso!", "success")
    return redirect(url_for('list_vendas'))

@app.route("/vendas")
def vendas():
    periodo_get = request.args.get("periodo")


    # consulta no banco usando periodo...
    periodos = {
    'today': '0 days',
    'last7days': '-6 days',
    'last30days': '-29 days',
    }

    periodo = periodos[periodo_get]

    list_regs = db_handle.db_query(
        '*',
        'fluxo_caixa',
        f"""WHERE data_hora_operacao >= datetime('now', 'localtime', '{periodo}', 'start of day')
        AND data_hora_operacao <= datetime('now', 'localtime')"""
    )

    total = 0
    for i in list_regs:
        total += i[1]

    return {"total": total}

#run

cli = logging.getLogger("werkzeug")
cli.setLevel(logging.ERROR)

if __name__ == '__main__':
    app.run(debug=False)