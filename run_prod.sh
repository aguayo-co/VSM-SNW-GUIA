#!/bin/sh

python manage.py migrate --noinput
python manage.py compilescss --use-storage
python manage.py collectstatic --no-input
python manage.py compilemessages
python manage.py update_index
gunicorn vsm_snw.wsgi -b 0.0.0.0:8000