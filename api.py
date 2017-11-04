import datetime
import random

import redis
from flask_restful import Resource
from flask import request

r = redis.Redis(decode_responses=True)

phrases = [
    '3dhubs',
    'marvin',
    'print',
    'filament',
    'order',
    'layer'
]


class Phrase(Resource):
    def get(self):
        phrase = random.choice(phrases)
        letters = [{'letter': l, 'revealed': False} for l in phrase]
        return {'phrase': {'letters': letters, 'errorCount': 0}}

    def post(self):
        letter = request.json['letter']
        phrase = request.json['phrase']
        error_count = phrase['errorCount']

        if letter not in [l['letter'] for l in phrase['letters']]:
            error_count += 1

        for phrase_letter in phrase['letters']:
            if phrase_letter['letter'] == letter:
                phrase_letter['revealed'] = True

        return {'phrase':
                {'letters': phrase['letters'], 'errorCount': error_count}}


def insert_score(score, username):
    # atomically increment the counter
    match_id = r.incr('score:sequence')
    match_object = {
        'id': match_id,
        'score': score,
        'username': username,
        'createdAt': datetime.datetime.today().isoformat()
    }

    r.hmset(f'score:data:{match_id}', match_object)

    # add the match_id to a sorted set
    r.zadd('score:table', match_id, score)

    return match_object


class Score(Resource):
    def post(self):
        score = request.json['score']
        username = request.json['username']

        return insert_score(score, username)

    def get(self):
        score_ids = r.zrevrangebyscore(
            'score:table', float('inf'), float('-inf'),
            start=0, num=10) 
        score_objects = [dict(r.hgetall('score:data:{}'.format(int(match_id))))
                         for match_id in score_ids]

        return {'scores': score_objects}
