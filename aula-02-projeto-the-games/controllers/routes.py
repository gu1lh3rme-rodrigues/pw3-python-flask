# Comentário em python
# Importando o pacote do Flask
from flask import render_template, request

jogadores = ['Black.Buterfly', 'Enderboy_404']
def init_app(app):
    @app.route('/')
    # Criando Função no Python
    def home():
        return render_template('index.html')

    # atividade do dia

    @app.route('/games', methods=['GET', 'POST'])
    # View function - Função de visualização
    def games():
        # dicionário no python (objeto)
        game = {'Titulo': 'CS-GO',
                'Ano': 2012,
                'Categoria': 'FPS Online'}

        if request.method == 'POST':
            if request.form.get('jogador'):  # nome do input
                jogadores.append(request.form.get('jogador'))

        jogos = ['Portal 2', 'Team Fortess 2', 'CS-GO', 'Half-Life',
                 'Dota', 'Day of Defeat:Source', 'Left 4 Dead']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)
