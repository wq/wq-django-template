define(['wq/app', 'wq/map', 'wq/patterns', 'wq/photos',
        './config',
        'leaflet.draw'],
function(app, map, patterns, photos, config) {

app.use(map);
app.use(patterns);
app.use(photos);

config.presync = presync;
config.postsync = postsync;
app.init(config).then(function() {
    app.jqmInit();
    app.prefetchAll();
});

// Sync UI
function presync() {
    $('button.sync').html("Syncing...");
    $('li a.ui-icon-minus, li a.ui-icon-alert')
       .removeClass('ui-icon-minus')
       .removeClass('ui-icon-alert')
       .addClass('ui-icon-refresh');
}

function postsync(items) {
    $('button.sync').html("Sync Now");
    app.syncRefresh(items);
}

});
