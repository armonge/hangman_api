from flask import Flask
from flask_restful import Api

from api import Phrase, Score


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Phrase, '/api/phrase')
    api.add_resource(Score, '/api/scores')

    return app


if __name__ == '__main__':
    app = create_app()
