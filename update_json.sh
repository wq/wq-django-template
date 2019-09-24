#!/bin/sh

set -e

VERSION=$1;

# Dump wq configuration object to file
{% if with_npm %}
mkdir -p app/src/tmpdata
db/manage.py dump_config > app/src/tmpdata/config.json
{% else %}
db/manage.py dump_config --format amd > app/js/data/config.js
{% endif %}

# Compile templates into fixture
cd app;
wq collectjson

# Update version.txt{% if with_npm %} and package.json{% endif %}
if [ "$VERSION" ]; then
    wq setversion $VERSION
    {% if with_npm %}
    echo "export default '$VERSION'" > src/tmpdata/version.js
    sed -i "s/\"version\":.*/\"version\": \"$VERSION\",/" package.json
    {% endif %}
fi;

{% if with_npm %}
# Move files at same time to trigger single react-scripts update
mv src/tmpdata/* src/data/;
rmdir src/tmpdata;
{% endif %}
cd ..;
