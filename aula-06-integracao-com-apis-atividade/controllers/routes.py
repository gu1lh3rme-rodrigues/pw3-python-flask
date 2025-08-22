from flask import render_template, request, url_for, redirect
import urllib
import json


def init_app(app):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        return render_template("index.html")
    
    @app.route('/api', methods=['GET', 'POST'])
    @app.route('/api/<id>', methods=['GET', 'POST'])
    def api(id=None):
        url = 'https://minecraft-api.vercel.app/api/items'
        response = urllib.request.urlopen(url   )
        apiData = response.read()
        mineInfolist = json.loads(apiData)
       # Se id existir
        if id:
            mineInfoInfo = []
            for mineInfo in mineInfolist:
                if mineInfo['namespacedId'] == id:
                    mineInfoInfo = mineInfo
                    break

            if mineInfo:
                return render_template('mineinfo.html', mineInfo=mineInfo)
            else:
                return f'Item com a ID {id} não existe'
        else:
            return render_template('api.html', mineInfolist=mineInfolist)
