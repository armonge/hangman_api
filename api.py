import random
from flask_restful import Resource
from flask import  request

phrases = [
    '3dhubs',
    'marvin',
    'print',
    'filament',
    'order',
    'layer'
];

class Phrase(Resource):
    def get(self):
        phrase = random.choice(phrases)
        letters = [{ 'letter': l, 'revealed': False} for l in phrase]
        return { 'phrase': { 'letters': letters, 'errorCount': 0 }}

    def post(self):
        letter = request.json['letter']
        phrase = request.json['phrase']
        error_count = phrase['errorCount']

        if not letter in [l['letter'] for l in phrase['letters']]:
            error_count += 1

        for phrase_letter in phrase['letters']:
            if phrase_letter['letter'] == letter:
                phrase_letter['revealed'] = True

        return { 'phrase': {'letters': phrase['letters'], 'errorCount': error_count}}

class Score(Resource):
    def post(self):
        pass

    def get(self):
        pass

