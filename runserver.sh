#!/bin/sh

set -e
. venv/bin/activate
echo "Starting Django..."
db/manage.py runserver &
{% if with_npm %}
sleep 10;
cd app
echo "Starting NPM..."
npm start
{% endif %}
