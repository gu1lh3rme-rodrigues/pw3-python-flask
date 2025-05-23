# Comentário em python
# Importando o pacote do Flask
from flask import render_template, request

jogadores = ['Black.Buterfly', 'Enderboy_404']

# array de objetosW
gamelist = [{'Título': 'CS-GO',
             'Ano': 2012,
             'Categoria': 'FPS Online'}]

Consoles = ['Nintendo', 'Xbox', 'Gameboy']

consolelist = [{'Nome': 'Xbox',
               'Preço': '10000',
                'País': 'EUA'}]


def init_app(app):
    @app.route('/')
    # Criando Função no Python
    def home():
        return render_template('index.html')

    # atividade do dia
# games
    @app.route('/games', methods=['GET', 'POST'])
    # View function - Função de visualização
    def games():
        # acessando o 1° jogo da lista de jogos
        game = gamelist[0]

        if request.method == 'POST':
            if request.form.get('jogador'):  # nome do input
                jogadores.append(request.form.get('jogador'))

        jogos = ['Portal 2', 'Team Fortess 2', 'CS-GO', 'Half-Life',
                 'Dota', 'Day of Defeat:Source', 'Left 4 Dead']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)

    # cadgames

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():

        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título': request.form.get('titulo'),
                                 'Ano': request.form.get('ano'),
                                 'Categoria': request.form.get('categoria')})

        return render_template('cadgames.html',
                               gamelist=gamelist)

# consoles
    @app.route('/consoles', methods=['GET', 'POST'])
    # View function - Função de visualização
    def consoles():
        # acessando o 1° jogo da lista de jogos
        console = consolelist[0]

        if request.method == 'POST':
            if request.form.get('console'):  # nome do input
                jogadores.append(request.form.get('console'))
# cadconsoles
    @app.route('/cadconsoles', methods=['GET', 'POST'])
    def cadconsoles():

        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('preço') and request.form.get('país'):
                consolelist.append({'Nome': request.form.get('Nome'),
                                    'Preço': request.form.get('Preço'),
                                    'País': request.form.get('País')})

                return render_template('cadconsole.html',
                                       consolelist=consolelist)
