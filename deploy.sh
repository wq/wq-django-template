#!/bin/sh

# Exit on error
set -e

# Build javascript with wq.app
cd app;
wq build $1;

# Force important files through any unwanted server caching
cd ../;
sed -i "s/{{project_name}}.js/{{project_name}}.js?v="$1"/" htdocs-build/{{project_name}}.appcache
sed -i "s/{{project_name}}.css/{{project_name}}.css?v="$1"/" htdocs-build/{{project_name}}.appcache

# Preserve Django's static files (e.g. admin)
cp -a htdocs/static htdocs-build/static

# Replace existing htdocs with new version
rm -rf htdocs/;
mv -i htdocs-build/ htdocs;

# Restart Django
touch db/{{project_name}}/wsgi.py
