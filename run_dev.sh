#!/bin/sh

echo "Running Django migrations (background job)" && \
python manage.py migrate --noinput
echo "Running Django Sass Compilation (background job)" && \
python manage.py compilescss --use-storage
echo "Running Django Static Collect (background job)" && \
python manage.py collectstatic --no-input
echo "Running Django Server" && \
python -Wd manage.py runserver --nostatic 0.0.0.0:8000