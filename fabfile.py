from fabric.api import env, run, prefix
from fabric.contrib.project import rsync_project


env.hosts = ['root@80.240.142.125']
RSYNC_EXCLUDES = ['local_settings.py', '.git', '*.pyc', 'htmlcov', 'mediafiles']


def rsync():
    rsync_project(remote_dir='/var/www/breakyourantiques', exclude=RSYNC_EXCLUDES, delete=True)


def start_server():
    run('sudo restart breakyourantiques')
    run('sudo start breakyourantiques')


def create_virtualenv():
    run('rm -rf /var/www/breakyourantiques/venv')
    run('virtualenv /var/www/breakyourantiques/venv')


def install():
    rsync()
    create_virtualenv()
    install_dependencies()
    run('rm /etc/nginx/sites-enabled/breakyourantiques')
    run('rm /etc/nginx/sites-available/breakyourantiques')
    run('cp /var/www/breakyourantiques/breakyourantiques/server-configuration/nginx /etc/nginx/sites-available/breakyourantiques')
    run('cp /var/www/breakyourantiques/breakyourantiques/server-configuration/upstart /etc/init/breakyourantiques.conf')
    run('ln -s /etc/nginx/sites-available/breakyourantiques /etc/nginx/sites-enabled')
    run('sudo start breakyourantiques')
    run('/etc/init.d/nginx restart')


def install_dependencies():
    with prefix('source /var/www/breakyourantiques/venv/bin/activate'):
        run('/var/www/breakyourantiques/venv/bin/pip install -r /var/www/breakyourantiques/breakyourantiques/requirements.txt -U')


def deploy():
    rsync()
    install_dependencies()
    start_server()
