#!/bin/sh

set -e

VERSION=$1;

# Dump wq configuration object to file
db/manage.py dump_config --format esm > app/{% if with_npm %}src{% else %}js{% endif %}/data/config.js

# Update version.txt{% if with_npm %} and package.json{% endif %}
if [ "$VERSION" ]; then
    wq setversion $VERSION
fi;
