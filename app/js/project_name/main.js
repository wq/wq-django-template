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
    },
    'run': function($page) {
        $page.find('form[data-wq-confirm]').on('submit', function() {
            return app.confirmSubmit(this, 'Are you sure you want to delete this record?');
        });
        $page.find('button[data-wq-action="sync"]').on('click', function() {
            app.retryAll();
        });
        $page.find('button[data-wq-action="empty-outbox"]').on('click', function() {
            app.emptyOutbox(true);
        });
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
