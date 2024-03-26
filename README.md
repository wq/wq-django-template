 Django project template for wq framework
=========================================

This is the recommended Django project template for projects utilizing the [wq framework].  It uses [wq.app] for the front end and [wq.db] as the backend component.   This template is meant to be used together with [wq.create].  See wq's [Getting Started] docs for more information.

When used with the `--with-npm` command for wq create, the app/ folder in this template will replaced with the contents of [wq-vite-template] (via [@wq/create]).

### Rationale

This project template is also useful as an example of how to build a web app with [React] and a [Django REST Framework] backend.  It differs from the default Django and vite templates in a few key ways:

 * Key front end files are kept in the `app/` folder, making it easier to customize the generated [installable PWA], and (optionally) to compile the front end with React Native or Expo for distribution on the app stores.
 * Because of this separation, the root of the Django project is in `db/` rather than at the top level of the project.
 * The root `ReactDOM.render()` call and Redux initialization are handled automatically by [@wq/react] and [@wq/store].  It is not necessary to explicitly define any React components, except to override the default [@wq/material] UI.
 * A default Apache2 WSGI configuration is included in `conf/`

[wq framework]: http://wq.io/
[wq.app]: https://wq.io/wq.app/
[wq.db]: https://wq.io/wq.db/
[wq.create]: https://wq.io/wq.create/
[Getting Started]: https://wq.io/overview/setup

[wq]: https://wq.io/wq
[@wq/app]: https://wq.io/@wq/app
[wq-vite-template]: https://github.com/wq/wq-vite-template
[@wq/create]: https://wq.io/@wq/create
[@wq/material]: https://wq.io/@wq/material
[@wq/react]: https://wq.io/@wq/react
[@wq/store]: https://wq.io/@wq/store

[React]: https://reactjs.org/
[Django REST Framework]: http://www.django-rest-framework.org
[installable PWA]: https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Installable_PWAs
