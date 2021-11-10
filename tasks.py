from celery import Celery
from celery.schedules import crontab

from made_topology import funcs_calls
from routers_ping import get_ping_rslt_dict_call


celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def ping_rslt_dict():
    rslt_dict = get_ping_rslt_dict_call()
    return rslt_dict


@celery_app.task
def formation_tplg():
    get_topology = funcs_calls()
    return get_topology


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), ping_rslt_dict.s())
    sender.add_periodic_task(crontab(minute='*/2'), formation_tplg.s())
