from wq.core import wq
import click
import sys
from pkg_resources import get_distribution


@wq.command()
@click.option("--output", help="Output filename")
@click.argument(
    "libraries",
    nargs=-1,
)
def versions(output, libraries):
    """
    List installed modules and their dependencies.
    Specify one or more libraries to show those dependencies instead.
    (Useful for generating a requirements.txt)
    """
    print_versions(output, libraries)


def print_versions(output, libraries):
    if not libraries:
        libraries = ['wq']
    libs = set()

    def add_lib(lib):
        dist = get_distribution(lib)
        libs.add((lib, dist.version))
        for req in dist.requires():
            add_lib(req.project_name)

    for lib in libraries:
        add_lib(lib)

    if output:
        dest = open(output, 'w')
    else:
        dest = sys.stdout

    for lib, version in sorted(libs):
        dest.write('%s==%s\n' % (lib, version))
