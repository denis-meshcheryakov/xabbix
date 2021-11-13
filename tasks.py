from celery import Celery
from celery.schedules import crontab

from made_topology import get_connect_dict_call
from routers_ping import get_ping_rslt_dict_call
from get_inventory import get_show_version_params_call


celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def ping_rslt_dict():
    rslt_dict = get_ping_rslt_dict_call()
    return rslt_dict


@celery_app.task
def formation_tplg():
    get_topology = get_connect_dict_call()
    return get_topology


@celery_app.task
def inventory_get():
    inventory = get_show_version_params_call()
    return inventory


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), ping_rslt_dict.s())
    sender.add_periodic_task(crontab(minute='*/1'), formation_tplg.s())
    sender.add_periodic_task(crontab(minute='*/1'), inventory_get.s())
