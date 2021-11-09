from celery import Celery
from celery.schedules import crontab

from formation_topology import get_connect_dict


celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def formation_tplg():
    get_connect_dict()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), formation_tplg.s())
