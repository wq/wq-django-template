 Django project template for wq framework
=========================================

This is the recommended Django project template for projects utilizing the [wq framework].  It uses [wq.app] for the front end and [wq.db] as the backend component.   This template is meant to be used together with [wq.create].  See wq's [Getting Started] docs for more information.

This template provides two alternatives for managing JavaScript dependencies ([@wq/app] & [wq.app]).  The alternatives can be selected by passing the `--with-npm` or `--without-npm` arguments to the `wq create` command.

 * `--with-npm`: `wq create` will generate an app/ folder based on the [@wq Create React App template][@wq/cra-template] and install [@wq/app] and [@wq/material] from NPM.
 * `--without-npm`: `wq create` will generate an app/ folder containing a minimal web-ready JavaScript configuration that can be merged with [wq.app]'s assets by running `./manage.py collectstatic`.  This leverages a new pre-compiled and minified ESM module, [**wq.js**](https://npmjs.com/package/wq), introduced in wq.app 1.3.

> Note: Existing RequireJS + jQuery Mobile + Mustache projects (created with wq.start 1.2 and earlier) will still work with wq.app 1.3.  However, wq.create 1.3 does not support creating new RequireJS projects.  Remaining support for RequireJS and jQuery Mobile will be removed in wq.app 2.0.

### Rationale

This project template is also useful as an example of how to build a web app with [React] and a [Django REST Framework] backend.  It differs from the default Django and Create React App templates in a few key ways:

 * Key front end files are kept in the `app/` folder, making it easier to customize the generated [installable PWA], and (optionally) to compile the front end with React Native or Expo for distribution on the app stores.
 * Because of this separation, the root of the Django project is in `db/` rather than at the top level of the project.
 * The root `ReactDOM.render()` call and Redux initialization are handled automatically by [@wq/react] and [@wq/store].  It is not necessary to explicitly define any React components, except to override the default [@wq/material] UI.
 * A default Apache2 WSGI configuration is included in `conf/`

[wq framework]: http://wq.io/
[wq.app]: https://wq.io/wq.app
[wq.db]: https://wq.io/wq.db
[wq.create]: https://wq.io/wq.create
[Getting Started]: https://wq.io/docs/setup

[@wq/app]: https://wq.io/docs/app-js
[@wq/cra-template]: https://github.com/wq/wq.create/tree/master/packages/cra-template
[@wq/material]: https://github.com/wq/wq.app/tree/master/packages/material
[@wq/react]: https://github.com/wq/wq.app/tree/master/packages/react
[@wq/store]: https://github.com/wq/wq.app/tree/master/packages/store

[React]: https://reactjs.org/
[Django REST Framework]: http://www.django-rest-framework.org
[installable PWA]: https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Installable_PWAs
