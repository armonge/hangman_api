from flask import Flask, request
from flask_restful import  Api

from  api import Phrase, Score

app = Flask(__name__)
api = Api(app)

api.add_resource(Phrase, '/api/phrase')
api.add_resource(Score, '/api/scores')
