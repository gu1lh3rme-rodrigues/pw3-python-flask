# Comentário em python
# Importando o pacote do Flask
from flask import Flask

from controllers import routes

# Carregando o Flask na Váriavel app
app = Flask(__name__, template_folder='views')

# Enviando o FLask (app) para a função init_app do routes
routes.init_app(app)

# Criando a rota principal do site

if __name__ == '__main__':
    # Rodando o Servidor do Localhost, na porta 5000
    app.run(host='localhost', port=5001, debug=True)
