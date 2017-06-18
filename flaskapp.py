from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app)


@api.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
