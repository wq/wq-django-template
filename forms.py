from wq.core import wq
import click
import os
from xlsconv import parse_xls, xls2django, xls2html, html_context, render
from pkg_resources import resource_filename
import subprocess
import json


templates = resource_filename('wq.start', 'master_templates')
# resource_filename not returning absolute path after pip install
if os.sep not in templates:
    import wq as wq_module
    templates = wq_module.__path__[0] + os.sep + templates


@wq.command()
@click.argument(
    "xlsform",
    required=True,
    type=click.Path(exists=True),
)
@click.option(
    "--input-dir",
    default="../master_templates",
    type=click.Path(exists=True),
    help="Source / master templates",
)
@click.option(
    "--django-dir",
    default=".",
    type=click.Path(exists=True),
    help="Root of Django project",
)
@click.option(
    "--template-dir",
    default="../templates",
    type=click.Path(exists=True),
    help="Path to shared template directory",
)
@click.option(
    "--form-name",
    help="Name to use for Django app and template prefix",
)
@click.option(
    "--with-admin/--no-admin",
    default=False,
    help="Generate admin.py",
)
def addform(xlsform, input_dir, django_dir, template_dir,
            form_name, with_admin):
    """
    Convert an XLSForm into a wq-compatible Django app, including:

    \b
        db/[form_name]/models.py
        db/[form_name]/rest.py
        templates/[form_name]_detail.html
        templates/[form_name]_edit.html
        templates/[form_name]_list.html
    """

    xls_json = parse_xls(xlsform)
    if not form_name:
        form_name = xls_json['name']

    os.mkdir(os.path.join(django_dir, form_name))

    create_file(
        [django_dir, form_name, 'models.py'],
        xls2django(xlsform)
    )
    create_file(
        [django_dir, form_name, 'rest.py'],
        xls2django(xlsform, os.path.join(templates, 'rest.py-tpl'))
    )
    if with_admin:
        create_file(
            [django_dir, form_name, 'admin.py'],
            xls2django(xlsform, os.path.join(templates, 'admin.py-tpl'))
        )

    template_types = set(['detail', 'edit', 'list'])
    for field in xls_json['children']:
        if 'geo' in field['type']:
            if 'popup' in template_types:
                print("Warning: multiple geometry fields found.")
            template_types.add('popup')
    for tmpl in template_types:
        create_file(
            [template_dir, "%s_%s.html" % (form_name, tmpl)],
            xls2html(xlsform, os.path.join(input_dir, '%s.html' % tmpl))
        )


@wq.command()
@click.option(
    "--input-dir",
    default="../master_templates",
    type=click.Path(exists=True),
    help="Source / master templates",
)
@click.option(
    "--django-dir",
    default=".",
    type=click.Path(exists=True),
    help="Root of Django project",
)
@click.option(
    "--template-dir",
    default="../templates",
    type=click.Path(exists=True),
    help="Path to shared template directory",
)
@click.option(
    '--overwrite/--no-overwrite',
    default=False,
    help="Replace existing templates",
)
def maketemplates(input_dir, django_dir, template_dir, overwrite):
    """
    Generate Mustache templates for all wq.db-registered models.

    \b
        templates/[model_name]_detail.html
        templates/[model_name]_edit.html
        templates/[model_name]_list.html
    """
    result = subprocess.check_output(
        [os.path.join(django_dir, 'manage.py'), 'dump_config']
    )
    config = json.loads(result.decode('utf-8'))

    for page in config['pages'].values():
        if not page.get('list', None):
            continue

        fields = []
        for field in page['form']:
            if field['type'] in ('repeat',):
                continue
            field['type_info'] = {'bind': {'type': field['type']}}
            fields.append(field)

        context = html_context({
            'name': page['name'],
            'title': page['name'],
            'children': fields,
        })
        context['form']['urlpath'] = page['url']

        template_types = set(['detail', 'edit', 'list'])
        for field in page['form']:
            if 'geo' in field['type']:
                if 'popup' in template_types:
                    print("Warning: multiple geometry fields found.")
                template_types.add('popup')
        for tmpl in template_types:
            create_file(
                [template_dir, "%s_%s.html" % (page['name'], tmpl)],
                render(context, os.path.join(input_dir, '%s.html' % tmpl)),
                overwrite=overwrite,
            )


def create_file(path, contents, overwrite=True):
    if os.path.exists(os.path.join(*path)) and not overwrite:
        print('%s already exists; skipping' % path[-1])
        return
    out = open(os.path.join(*path), 'w')
    out.write(contents)
    out.close()
