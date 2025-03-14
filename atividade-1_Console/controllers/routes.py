from flask import render_template, request

Consoles = ['Nintendo', 'Xbox', 'Gameboy']

consolelist= [{'Nome': 'Xbox',
               'Preço': '10000', 
               'País': 'EUA'}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route ('/consoles', methods= ['GET', 'POST'])
    def consoles(): 

        consoles = consolelist[0]

        if request.method == 'POST':
            if request.form.get('Consoles'):   
                Consoles.append(request.form.get('Consoles'))

                @app.route('/cadconsoles', methods= ['GET', 'POST'])
                def cadconsoles():

                    if request.method == 'POST':
                        if request.form.get('nome') and request.form.get ('preço') and request.form.get ('país'):
                            consolelist.append ({'Nome': request.form.get('Nome'),
                                                 'Preço': request.form.get('Preço'),
                                                 'País': request.form.get('País')})
                            
                            return render_template ('cadconsole.html',
                                                    consolelist = consolelist)