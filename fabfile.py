from __future__ import with_statement
from fabric.api import run, cd, env

env.forward_agent = True
env.shell = "/bin/bash -l -i -c" 

def deploy_api():
    with cd('hangman_api'):
        run('git pull origin master')
        run('forever restartall')

def deploy_frontend():
    with cd('hangman'):
        run('git pull origin master')
        run('ng build --prod')

