import db_handle as db_handle
from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask('app.py')
app.config["SECRET_KEY"] = "wlsec"


#rendereizar estoque;
@app.route('/')
def index():
    return redirect(url_for('estoque')) 


#cadastr. produtos
#acho q teria q usar lib request e verificar se é post
@app.route('/cadastrar',methods=["GET","POST"])
def cad():
    if request.method == "POST":
        nome = request.form.get('nome_produto')
        valor = request.form.get('valor_produto')
        qtd = request.form.get('qtd_produto')
    
        db_handle.db_insert('produtos',(nome,valor,qtd))

        #indicar sucesso
        flash("Produto cadastrado com sucesso!", "success") 
        return redirect(url_for("cad"))
    
    elif request.method.lower() == 'get':
        return render_template('cadastrar.html')
        

@app.route('/estoque')
def estoque():
    lista_dados = db_handle.db_query('*','produtos')
    return render_template('estoque.html',context=lista_dados)


#run
app.run(debug=True)
