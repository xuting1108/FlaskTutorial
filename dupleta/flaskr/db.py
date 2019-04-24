import sqlite3

import click
from flask import current_app, g #g é um objeto especial que é exclusivo para cada solicitação. Ele é usado para armazenar dados que podem ser acessados ​​por várias funções durante a solicitação.
#current_app: aponta para o aplicativo Flask que manipula a solicitação
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        #estabelece uma conexão com o arquivo apontado pela DATABASEchave de configuração.
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row#informa a conexão para retornar linhas que se comportam como dicts. Isso permite acessar as colunas por nome.

    return g.db

#verifica se uma conexão foi criada, verificando se g.db foi definida. Se a conexão existir, ela será fechada. 
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f: #as = alias = apelido
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')#define um comando de linha de comando chamado init-db que chama a init_dbfunção e mostra uma mensagem de sucesso ao usuário. 
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)#diz ao Flask para chamar essa função ao limpar depois de retornar a resposta.
    app.cli.add_command(init_db_command)#adiciona um novo comando que pode ser chamado com o flaskcomando.