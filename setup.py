import os
from setuptools import setup

LONG_DESCRIPTION = """
Django project template for building REST-ful web & hybrid apps with wq.app and wq.db.
"""


def parse_markdown_readme():
    """
    Convert README.md to RST via pandoc, and load into memory
    (fallback to LONG_DESCRIPTION on failure)
    """
    # Attempt to run pandoc on markdown file
    import subprocess
    try:
        subprocess.call(
            ['pandoc', '-t', 'rst', '-o', 'README.rst', 'README.md']
        )
    except OSError:
        return LONG_DESCRIPTION

    # Attempt to load output
    try:
        readme = open(os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        ))
    except IOError:
        return LONG_DESCRIPTION
    return readme.read()


def create_wq_namespace():
    """
    Generate the wq namespace package
    (not checked in, as it technically is the parent of this folder)
    """
    if os.path.isdir("wq"):
        return
    os.makedirs("wq")
    init = open(os.path.join("wq", "__init__.py"), 'w')
    init.write("__import__('pkg_resources').declare_namespace(__name__)")


def list_package_data(root):
    """
    Include project template as package data
    """
    paths = []
    for base, dirs, files in os.walk(root):
        paths.extend([os.path.join(base, name) for name in files])
    return paths


create_wq_namespace()

# Template data (currently only one project template)
TEMPLATES = [
    'django_project',
]
TEMPLATE_DATA = []
for folder in TEMPLATES:
    TEMPLATE_DATA.extend(list_package_data(folder))

setup(
    name='wq.start',
    version='0.8.1',
    author='S. Andrew Sheppard',
    author_email='andrew@wq.io',
    url='http://wq.io/',
    license='MIT',
    description=LONG_DESCRIPTION.strip(),
    long_description=parse_markdown_readme(),
    entry_points={'wq':'wq.start=wq.start'},
    packages=['wq.start'],
    package_dir={'wq.start': '.'},
    namespace_packages=['wq'],
    package_data={'wq.start': TEMPLATE_DATA},
    install_requires=[
        'wq.core',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: JavaScript',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Pre-processors',
    ]
)
