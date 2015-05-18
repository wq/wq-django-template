define(['wq/app', 'wq/map', './config'],
function(app, map, config) {

app.init(config).then(function() {
    map.init(config.map);
    app.jqmInit();
});

});
