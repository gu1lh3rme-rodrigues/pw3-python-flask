# Comentário em python
# Importando o pacote do Flask
from flask import Flask

# Carregando o Flask na Váriavel app
app = Flask(__name__)

#Criando a rota principal do site
@app.route ('/')
#Criando Função no Python
def home():
    return '<h1>Meu primeiro site em Flask. Seja bem-vindo!<br><br>É isso apenas</h1>'

# #atividade do dia 
# @app.route('/')
# def games():
#     return '<h1>Seja bem vindo a página de Games</h1>'
if __name__ == '__main__':
    #Rodando o Servidor do Localhost, na porta 5000
    app.run(host='localhost', port = 5000, debug=True)