# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, World!'

from flask import Flask
app = Flask(__name__)

#decorator(aplica uma funcao emcima de outra)
@app.route("/")#quando acessar essa rota, sera exibido o hello world como conteudo
def hello():
    return u'Olá mundo!'

if __name__ == "__main__":# questao de segurança para verificar se o usuario está executando o arquivo principal
    app.run()