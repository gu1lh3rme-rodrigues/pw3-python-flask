# pip gerenciador de pacotes do python
# pip install flask
# importando pacote do Flask
from flask import Flask
# importando arquivo routes do controllers
from controllers import routes
# importando o PyMySql
import pymysql
#importando o model Game
from models.database import db

# carregando o Flask na variável app
app = Flask(__name__, template_folder="views")

# Enviando o Flask (app) para a função init_app do routes
routes.init_app(app)

DB_NAME = 'games'
# configura o flask com o banco definido
app.config['DATABASE_NAME'] = DB_NAME
# Passando o endereco ao Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:admin@localhost/{DB_NAME}'

if __name__ == '__main__':
    # criando os dados de conexao
    connection = pymysql.connect(host='localhost',
                                 user=' root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass='pymysql.cursor.'
                                 'DictCursor')
    # Tentando criar o banco
    # try: trata o sucesso
    try:
        # with cria um recurso temporariamente
        with connection.cursor() as cursor:
            # Cria o banco de dados (se ele não existir)
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O Banco de Dados {DB_NAME} está criado!")

        # Except: trata a falha
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")

    finally:
        connection.close()
        #passando o flask para o sqlalchemy
        db.init_app(app=app)
        #criando as tabelas a partir do model
        with app.test_request_context():
            db.create_all()
            
    # Rodando o servidor no localhost, porta 5000
    app.run(host='0.0.0.0', port=5001, debug=True)
