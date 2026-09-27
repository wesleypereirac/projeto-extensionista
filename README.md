# Projeto Extensionista - Gestão de Estoque e Vendas

Este projeto foi desenvolvido como parte de uma Atividade Extensionista e tem como objetivo auxiliar o gerenciamento de produtos em estoque e o registro de valores das vendas.

A aplicação utiliza HTML, CSS, JavaScript e Python e permite realizar o cadastro e gerenciamento de produtos, o controle do estoque e o registro das vendas realizadas. Este repositório contém o código-fonte e as instruções necessárias para executar o projeto localmente.

# Setup - Comandos de terminal

## Dependências
- Ferramentas Python e Git já instaladas

## Baixar repositório e criar ambiente virtual
```bash
git clone https://github.com/wesleypereirac/projeto-extensionista/
cd projeto-extensionista/core
python -m venv venv
```

## Ativação do venv:
### Para Linux/Mac
```bash
source venv/bin/activate
```

### Para Windows 
::(PowerShell)
```bash
venv\Scripts\Activate.ps1
```
:: (CMD)
```bash
venv\Scripts\activate.bat
```


## Instalar as dependências e rodar servidor
```bash
pip install -r requirements.txt

python app.py
```

## Abrir url do site local
- Acessar [localhost:5000](http://localhost:5000)
- Com o repo configurado uma vez, nas próximas inicializações basta [ativar o venv](#ativação-do-venv) e rodar o comando abaixo:
```bash
python app.py
```
