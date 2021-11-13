#!/bin/sh
sudo service redis-server start
celery -A tasks worker -B --loglevel=INFO