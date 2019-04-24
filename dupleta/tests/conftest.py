import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()#cria e abre um arquivo temporário, retornando o objeto de arquivo e o caminho para ele.

    app = create_app({
        'TESTING': True, #TESTINGdiz ao Flask que o aplicativo está no modo de teste. O Flask altera alguns comportamentos internos para facilitar o teste, e outras extensões também podem usar o sinalizador para facilitar o teste.
        'DATABASE': db_path,#O DATABASEcaminho é sobrescrito, então aponta para este caminho temporário ao invés da pasta da instância. Depois de definir o caminho, as tabelas do banco de dados são criadas e os dados de teste são inseridos. 
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)