from fabric.api import env, run, prefix
from fabric.contrib.project import rsync_project


env.hosts = ['root@80.240.142.125']
RSYNC_EXCLUDES = ['local_settings.py', '.git', '*.pyc', 'htmlcov', 'mediafiles', 'server', 'celerybeat-schedule']


def rsync():
    rsync_project(remote_dir='/var/www/breakyourantiques/breakyourantiques', exclude=RSYNC_EXCLUDES, delete=True)


def install_dependencies():
    with prefix('source /www/backend/venv/bin/activate'):
        run('/var/www/breakyourantiques/venv/bin/pip install -r /var/www/breakyourantiques/breakyourantiques/requirements.txt -U')


def deploy():
    rsync()
    install_dependencies()
