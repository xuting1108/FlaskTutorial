# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, World!'

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return u'Olá mundo!'

if __name__ == "__main__":
    app.run()