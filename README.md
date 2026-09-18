- breve descrição
- passos para iniciar (server, etc e urls:porta)

# setup

## entrar na pasta do sistema
git clone https://github.com/wesleypereirac/projeto-extensionista/
cd projeto-extensionista/core

## Criar o ambiente virtual
python -m venv venv

## Ativar o venv (escolher de acordo com o sistema)

- Linux/Mac: source venv/bin/activate

- Windows: venv\Scripts\activate

## Instalar as dependências
pip install -r requirements.txt

# usage

- dentro de projeto-extensionista/core
- python app.py
- acessar localhost:5000

# Observações
- O banco de dados não é versionado, é criado localmente. 