requirejs.config({
    'baseUrl': '/js/lib',
    'paths': {
        '{{ project_name }}': '../{{ project_name }}',
        'db': '../../'
    }
});

requirejs(['{{ project_name }}/main']);
