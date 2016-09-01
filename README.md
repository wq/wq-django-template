 Django project template for wq framework
=========================================

This is the recommended Django project template for projects utilizing the [wq framework], with [wq.app] for the front end and [wq.db] as the backend component.   This template is meant to be used together with [wq.start].  See the [Getting Started] docs for more information.

### Rationale

This project template is also useful as an example of how to build a web app with [RequireJS] and a [Django REST Framework] backend.  It differs from the default Django project template in a few key ways:

 * A default Apache2 WSGI configuration is included in `conf/`
 * All static files are kept in the `app/` folder, with the idea that they will be built with a RequireJS-powered [build process].  This clean separation between the front end and backend components makes it easier to wrap the front end in [PhoneGap] for release on app stores.
 * Because of this separation, the root of the Django project is in `db/` rather than at the top level of the project.  `db/` is included on the Python path in the Apache config (and implicitly when running `./manage.py`).
 * Mustache templates are kept at the top level, because they are [shared between the client and the server](http://wq.io/docs/templates).

[wq framework]: http://wq.io/
[wq.app]: https://wq.io/wq.app
[wq.db]: https://wq.io/wq.db
[wq.start]: https://wq.io/wq.start
[Getting Started]: https://wq.io/docs/setup
[RequireJS]: http://requirejs.org
[Django REST Framework]: http://www.django-rest-framework.org
[build process]: http://wq.io/docs/build
[PhoneGap]: http://phonegap.com
