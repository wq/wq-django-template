import wq from './wq.js';
import config from './data/config.js';
// import config from '/config.js';  // Load directly from wq.db


async function init() {
    await wq.init(config);
    await wq.prefetchAll();
    if (config.debug) {
        window.wq = wq;
    }
}

init();

navigator.serviceWorker.register('/service-worker.js');
