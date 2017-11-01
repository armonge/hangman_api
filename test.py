'''
Couple small tests for the simple hangman api
'''
import json

import pytest

from app import create_app


@pytest.fixture
def app():
    '''Standard fixture used by pytest-flask'''
    return create_app()


def test_initial_phrase_is_unrevealed(client):
    ''' Test initial phrase is always unrevealed '''
    response = client.get('/api/phrase')
    assert not any([l['revealed'] for l in response.json['phrase']['letters']])


def test_initial_error_count_is_zero(client):
    ''' Test initial error count is always initialized to 0 '''
    response = client.get('/api/phrase')
    assert response.json['phrase']['errorCount'] == 0


def test_reveals_correct_letters(client):
    ''' Sends a post and checks correct letters are revealed '''
    request_body = {'letter': 'p', 'phrase': {'letters': [{'letter': 'p', 'revealed': False}, {'letter': 'r', 'revealed': False}, {
        'letter': 'i', 'revealed': False}, {'letter': 'n', 'revealed': False}, {'letter': 't', 'revealed': False}], 'errorCount': 0}}

    response = client.post(
        '/api/phrase', data=json.dumps(request_body),
        content_type='application/json')
    assert response.json['phrase']['errorCount'] == 0
    assert response.json['phrase']['letters'] == [
        {'letter': 'p', 'revealed': True},
        {'letter': 'r', 'revealed': False},
        {'letter': 'i', 'revealed': False},
        {'letter': 'n', 'revealed': False},
        {'letter': 't', 'revealed': False}]
