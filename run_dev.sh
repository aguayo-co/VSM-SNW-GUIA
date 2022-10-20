#!/bin/sh

python manage.py migrate --noinput
python manage.py compilescss --use-storage
python manage.py collectstatic --no-input
python manage.py compilemessages
python -Wd manage.py runserver --nostatic 0.0.0.0:8000