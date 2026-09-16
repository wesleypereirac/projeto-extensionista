import db_handle as db_handle
from flask import Flask, request, render_template, flash, redirect, url_for

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

@app.route('/deletar', methods=['POST'])
def deletar():
    id_produto = request.form.get('id')

    db_handle.db_delete('produtos', id_produto)  # adapte para sua função

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
@app.route('/registrar_venda', methods=['GET', 'POST'])
def reg_venda():

    if request.method == "POST":
        valor = request.form.get('valor_venda')
        db_handle.db_insert_or_update_qtd('fluxo_caixa',(valor))
        flash("Venda registrada com sucesso!", "success") 
        return redirect(url_for("reg_venda"))
    
    else:
        return render_template('fluxo_vendas.html')


#run
app.run(debug=True)
