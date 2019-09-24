function getBaseUrl() {
    var baseurl = window.location.pathname.replace("index.html",'');
    baseurl = baseurl.replace(/\/$/,'');
    if (baseurl == 'www') {
        // Windows
        baseurl = '/www';
    }
    return baseurl;
}

window.WQ_CONFIG = {
    'router': {
        'base_url': getBaseUrl()
    },
    'store': {
        'service': 'https://{{ domain }}',
        'defaults': {'format': 'json'}
    },
    'onReady': onReady;
};

function onReady(app) {
    app.replaceState('');
    setTimeout(navigator.splashscreen.hide, 10);
}
