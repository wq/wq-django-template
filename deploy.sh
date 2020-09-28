#!/bin/sh

# Exit on error
set -e

VERSION=$1;

if [ -z "$VERSION" ]; then
    echo "Usage: ./deploy.sh [VERSION]"
    exit 1
fi;

# Regenerate JSON fixtures
./update_json.sh $VERSION;

wq icons;
{% if with_npm %}
# Build using react-scripts (Webpack/Babel)
cd app;
npm run build;

# Update existing htdocs with new version
cd ..;
mkdir -p htdocs/
cp -a app/build/* htdocs/
{% else %}
# Collect static app files
wq build $VERSION
db/manage.py collectstatic --no-input
mv htdocs/static/app/public/*.* htdocs/
wq serviceworker $VERSION
{% endif %}

# Restart Django
touch db/{{project_name}}/wsgi.py
