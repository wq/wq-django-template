define(["data/config", "data/templates", "data/version", "module"],
function(config, templates, version, module) {

var overrides = module.config();

config.version = version;

config.router = {
    'base_url': ''
};

config.template = {
    'templates': templates,
};

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

return config;

});
