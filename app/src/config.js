import config from './data/config.json';
import templates from './data/templates.json';
import version from './data/version';

var overrides = window.cordova ? (window.WQ_CONFIG || {}) : {};

config.version = version;

config.router = {
    'base_url': ''
};

config.template = { templates };

config.store = {
    'service': config.router.base_url,
    'defaults': {'format': 'json'}
};

config.map = {
    'bounds': [[44.7, -93.6], [45.2, -92.8]]
};

config.outbox = {};

config.transitions = {
    'default': "none"
};

for (var key in overrides) {
    config[key] = overrides[key];
}

export default config;
