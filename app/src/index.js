import app, { patterns, photos } from '@wq/app';
import map from '@wq/map';
import config from './config';
import * as serviceWorker from './serviceWorker';

app.use(map);
app.use(patterns);
app.use(photos);
app.use({
    context() {
        const { version } = config;
        return { version };
    }
});

var ready = app.init(config).then(function() {
    app.jqmInit();
    app.prefetchAll();
});

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

if (config.debug) {
    window.wq = app;
}

if (config.onReady) {
    ready.then(function() {
	config.onReady(app);
    });
}
