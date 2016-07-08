from wq.core import wq
import click
import os
from xlsconv import parse_xls, xls2django, xls2html, html_context, render
from pkg_resources import resource_filename
import subprocess
import json
from difflib import unified_diff


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

    if not os.path.exists(os.path.join(django_dir, form_name)):
        os.mkdir(os.path.join(django_dir, form_name))

    create_file(
        [django_dir, form_name, 'models.py'],
        xls2django(xlsform, 'models')
    )

    has_nested = False
    for field in xls_json['children']:
        if field.get('wq:nested', False):
            has_nested = True
    if has_nested:
        create_file(
            [django_dir, form_name, 'serializers.py'],
            xls2django(xlsform, 'serializers'),
        )

    create_file(
        [django_dir, form_name, 'rest.py'],
        xls2django(xlsform, 'rest'),
    )
    if with_admin:
        create_file(
            [django_dir, form_name, 'admin.py'],
            xls2django(xlsform, 'admin'),
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
            xls2html(xlsform, tmpl),
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
    '-f',
    '-overwrite',
    default=False,
    is_flag=True,
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

        def process_fields(fields):
            for field in fields:
                if field['type'] in ('repeat',):
                    field['wq:nested'] = True
                    process_fields(field['children'])
                else:
                    field['type_info'] = {'bind': {'type': field['type']}}

        process_fields(page['form'])
        context = html_context({
            'name': page['name'],
            'title': page['name'],
            'children': page['form'],
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


def create_file(path, contents, overwrite=False):
    filename = os.path.join(*path)
    if os.path.exists(filename) and not overwrite:
        existing_file = open(filename, 'r')
        existing_content = existing_file.read()
        if existing_content.strip() == contents.strip():
            return
        choice = ''
        while choice.lower() not in ('y', 'n'):
            choice = click.prompt(
                '%s already exists; overwrite? [y/n/d/?]' % path[-1]
            )
            if choice.lower() == 'n':
                return
            elif choice.lower() == '?':
                print(
                    '  y - overwrite\n'
                    '  n - skip\n'
                    '  d - show diff\n'
                    '  ? - show help'
                )
            elif choice.lower() == 'd':
                diff = unified_diff(
                    existing_content.split('\n'),
                    contents.split('\n'),
                    fromfile="%s (current)" % path[-1],
                    tofile="%s (new)" % path[-1],
                )
                for row in diff:
                    print(row)
    out = open(os.path.join(*path), 'w')
    out.write(contents)
    out.close()
