#!/bin/sh

set -e

python manage.py collectstatic --noinput

uwsgi --socket 0.0.0.0:8000 --master --enable-threads --module freelancer.wsgi