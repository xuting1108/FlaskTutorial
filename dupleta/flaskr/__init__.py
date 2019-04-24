import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    # __name__é o nome do módulo Python atual. O aplicativo precisa saber onde ele está localizado para configurar alguns caminhos e __name__é uma maneira conveniente de informar isso.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',#manter os dados seguros
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),#o caminho onde o arquivo de banco de dados SQLite será salvo.
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)#substitui a configuração padrão por valores obtidos do config.py arquivo na pasta da instância, se existir
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)#O Flask não cria a pasta de instâncias automaticamente, mas ela precisa ser criada porque o seu projeto criará o arquivo de banco de dados SQLite lá.
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')#Ele cria uma conexão entre a URL /helloe uma função que retorna uma resposta, a string neste caso.'Hello, World!'
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

    


