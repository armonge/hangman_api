from __future__ import with_statement
from fabric.api import run, cd, env, prefix

env.forward_agent = True
env.shell = "/bin/bash -l -i -c" 

def deploy_api():
    with cd('hangman_api'):
        run('git pull origin master')
        with prefix('source env/bin/activate'):
            run('pip install -r requirements.txt')
            run('forever stopall')
            run('FLASK_APP=app.py forever start --sourceDir $HOME/hangman_api -c python env/bin/flask run')

def deploy_frontend():
    with cd('hangman'):
        run('git pull origin master')
        run('ng build --prod')


def read_api_logs():
    log_path = run("forever --plain logs | grep flask | awk '{print $4}'")
    print(log_path)
    run('cat "{}"'.format(log_path))
