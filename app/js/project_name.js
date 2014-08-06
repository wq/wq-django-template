requirejs.config({
    'baseUrl': '/js/lib',
    'paths': {
        '{{ project_name }}': '../{{ project_name }}',
        'data': '../data/',
        'db': '../../'
    }
});

requirejs(['{{ project_name }}/main']);
