from wq.core import wq
import click
import os
from django.core.management import call_command
import sys
from pkg_resources import resource_filename, get_distribution

template = resource_filename('wq.start', 'django_project')
# resource_filename not returning absolute path after pip install
if os.sep not in template:
    import wq as wq_module
    template = wq_module.__path__[0] + os.sep + template


@wq.command()
@click.argument("project_name", required=True)
@click.argument("destination", required=False)
def start(project_name, destination):
    """
    Start a new project with wq.app and wq.db.  A new Django project will be
    created from a wq-specific template.  After running this command, you may
    want to do the following:

    \b
        sudo chown www-data media/
        cd app
        wq init

    See https://wq.io/docs/setup for more tips on getting started with wq.
    """
    call_command(
        'startproject',
        project_name,
        destination,
        template=template,
        extensions=["py", "yml", "conf", "html", "sh", "js", "css", "json"],
    )
    txt = os.path.join(destination or project_name, 'requirements.txt')
    print_versions(txt, False)


@wq.command()
@click.option("--output", help="Output filename")
@click.option(
    "--all/--app-db-only",
    default=False,
    help="Include all wq deps, or only those required for wq.app and wq.db."
)
def versions(output, all):
    """
    Show installed versions of wq.app and wq.db.  Also prints out
    any and all required dependencies.

    (Useful for generating a requirements.txt)
    """
    print_versions(output, all)


def print_versions(output, all):
    libs = set()

    def add_lib(lib):
        dist = get_distribution(lib)
        libs.add((lib, dist.version))
        for req in dist.requires():
            add_lib(req.project_name)

    if all:
        init_libs = ['wq']
    else:
        init_libs = ['wq.app', 'wq.db']
    for lib in init_libs:
        add_lib(lib)

    if output:
        dest = open(output, 'w')
    else:
        dest = sys.stdout

    for lib, version in sorted(libs):
        dest.write('%s==%s\n' % (lib, version))
