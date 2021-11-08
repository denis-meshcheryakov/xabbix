from celery import Celery
from celery.schedules import crontab

from formation_topology import get_connect_dict

from webapp import create_app

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def formation_tplg():
    with flask_app.app_context():
        get_connect_dict()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/2'), get_connect_dict.s())

