#!/bin/sh

# Exit on error
set -e

VERSION=$1;

if [ -z "$VERSION" ]; then
    echo "Usage: ./deploy.sh [VERSION]"
    exit 1
fi;

# (Re-)generate templates for all registered models
wq maketemplates \
     --django-dir db \
     --input-dir master_templates \
     --template-dir templates

# Regenerate JSON fixtures
./update_json.sh $VERSION;

cd app;
wq icons;

{% if with_npm %}
wq init;
wq scss;

# Build using react-scripts (Webpack/Babel)
npm run build;

# Update existing htdocs with new version
cd ..;
mkdir -p htdocs/
cp -a app/build/* htdocs/
{% else %}
# Build javascript with wq.app
wq build $VERSION

# Force important files through any unwanted server caching
cd ../;
sed -i "s/{{project_name}}.js/{{project_name}}.js?v="$1"/" htdocs-build/{{project_name}}.appcache
sed -i "s/{{project_name}}.css/{{project_name}}.css?v="$1"/" htdocs-build/{{project_name}}.appcache

# Preserve Django's static files (e.g. admin)
if [ -d htdocs/static ]; then
    cp -a htdocs/static htdocs-build/static
fi;

# Replace existing htdocs with new version
rm -rf htdocs;
mv -i htdocs-build/ htdocs;
{% endif %}

# Restart Django
touch db/{{project_name}}/wsgi.py

# Build PhoneGap application
cd app;
wq phonegap $1
cd ../;
