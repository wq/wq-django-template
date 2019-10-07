define(['wq/app', 'wq/map', 'wq/patterns', 'wq/photos',
        './config',
        'leaflet.draw', 'leaflet.markercluster'],
function(app, map, patterns, photos, config) {

app.use(map);
app.use(patterns);
app.use(photos);
app.use({
    'context': function() {
        return {
            'version': config.version
        };
    }
});

var ready = app.init(config).then(function() {
    app.jqmInit();
    app.prefetchAll();
});


if (config.debug) {
    window.wq = app;
}

return ready;

});
