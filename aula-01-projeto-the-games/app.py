# Comentário em python
# Importando o pacote do Flask
from flask import Flask, render_template

# Carregando o Flask na Váriavel app
app = Flask(__name__, template_folder='views')

# Criando a rota principal do site


@app.route('/')
# Criando Função no Python
def home():
    return render_template('index.html')

# atividade do dia


@app.route('/games')
# View function - Função de visualização
def games():
    # dicionário no python (objeto)
    game = {'Titulo': 'CS-GO',
            'Ano': 2012,
            'Categoria': 'FPS Online'}
    jogadores = ['Black.Buterfly', 'Enderboy_404']
    jogos = ['Portal 2', 'Team Fortess 2', 'CS-GO', 'Half-Life',
             'Dota', 'Day of Defeat:Source', 'Left 4 Dead']
    return render_template('games.html',
                          game = game, 
                           jogos=jogos)


if __name__ == '__main__':
    # Rodando o Servidor do Localhost, na porta 5000
    app.run(host='localhost', port=5000, debug=True)

