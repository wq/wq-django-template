#!/bin/sh
set -e
db/manage.py deploy $1
touch db/{{project_name}}/wsgi.py
