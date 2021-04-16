import wq from './wq.js';
import config from './data/config.js';
import version from './data/version.js';

wq.use({
    context() {
        return { version };
    }
});

wq.init({
    ...config,
    router: {
        'base_url': ''
    },
    store: {
	'service': '',
	'defaults': {'format': 'json'}
    },
    material: {
        theme: {
            primary: '#7500ae',
            secondary: '#0088bd'
        }
    },
    map: {
	bounds: [[-93.6, 44.7], [-92.8, 45.2]]
    }
}).then(() => {
    wq.prefetchAll();
});

if (config.debug) {
    window.wq = wq;
}

navigator.serviceWorker.register('/service-worker.js');
