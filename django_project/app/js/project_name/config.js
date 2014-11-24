define(["data/config", "data/version"],
function(config, version) {

config.defaults = {
    'version': version
};

config.transitions = {
    'default': "slide",
    'save': "flip"
};

return config;

});
