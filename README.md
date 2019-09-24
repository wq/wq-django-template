 Django project template for wq framework
=========================================

This is the recommended Django project template for projects utilizing the [wq framework].  It uses [wq.app] for the front end and [wq.db] as the backend component.   This template is meant to be used together with [wq.start].  See wq's [Getting Started] docs for more information.

As of version 1.2, this template provides two alternatives for managing JavaScript dependencies ([@wq/app]/[wq.app]).  The alternatives can be selected by passing the `--with-npm` or `--without-npm` arguments to the `wq start` command.

 * `--with-npm`: `wq start` will generate an app/ folder based on [Create React App][create-react-app] and install [@wq/app] from NPM.
 * `--without-npm`: `wq start` will generate an app/ folder with a [RequireJS]-compatible layout and use the AMD-format JavaScript libraries included in the [wq.app] PyPI package.  (This was the default and only option in wq 1.1 and earlier.)

### Rationale

This project template is also useful as an example of how to build a web app with [Create React App][create-react-app] (or [RequireJS]) and a [Django REST Framework] backend.  It differs from the default Django and Create React App templates in a few key ways:

 * Most front end files are kept in the `app/` folder, with the idea that they will be built with react-scripts (or RequireJS).  This clean separation between the front end and backend components makes it easier to wrap the front end in [PhoneGap] for release on app stores.
 * Because of this separation, the root of the Django project is in `db/` rather than at the top level of the project.
 * Mustache templates are in the top level folder `templates/`, because they are [shared between the client and the server](http://wq.io/docs/templates).
 * A default Apache2 WSGI configuration is included in `conf/`

See the [Create React App documentation][create-react-app] for more information on the available NPM scripts.

[wq framework]: http://wq.io/
[wq.app]: https://wq.io/wq.app
[@wq/app]: https://wq.io/docs/app-js
[wq.db]: https://wq.io/wq.db
[wq.start]: https://wq.io/wq.start
[Getting Started]: https://wq.io/docs/setup
[create-react-app]: https://facebook.github.io/create-react-app/docs/getting-started
[RequireJS]: http://requirejs.org
[Django REST Framework]: http://www.django-rest-framework.org
[build process]: http://wq.io/docs/build
[PhoneGap]: http://phonegap.com
