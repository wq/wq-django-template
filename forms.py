from wq.core import wq
import click
import os
from xlsconv import parse_xls, xls2django, xls2html
from pkg_resources import resource_filename


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
    default="master_templates",
    type=click.Path(exists=True),
    help="Source / master templates",
)
@click.option(
    "--django-dir",
    default="db",
    type=click.Path(exists=True),
    help="Root of Django project",
)
@click.option(
    "--template-dir",
    default="templates",
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

    if not form_name:
        xls_json = parse_xls(xlsform)
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

    for tmpl in ('detail', 'edit', 'list'):
        create_file(
            [template_dir, "%s_%s.html" % (form_name, tmpl)],
            xls2html(xlsform, os.path.join(input_dir, '%s.html' % tmpl))
        )


def create_file(path, contents):
    out = open(os.path.join(*path), 'w')
    out.write(contents)
    out.close()
