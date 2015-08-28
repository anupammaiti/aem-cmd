# coding: utf-8
import os.path

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

from acmd import __version__


class InstallBashCompletionDevelop(develop):
    def run(self):
        develop.run(self)
        deploy_bash_completion()


class InstallBashCompletion(install):
    def run(self):
        install.run(self)
        deploy_bash_completion()


def deploy_bash_completion():
    print "Running custom code!"
    path = locate_bash_completion_dir()
    if path is not None:
        install_script(path)


DEFAULT_COMPLETION_DIR = '/etc/bash_completion.d'
HOMEBREW_COMPLETION_DIR = '/usr/local/etc/bash_completion.d'


def locate_bash_completion_dir():
    alternatives = [DEFAULT_COMPLETION_DIR, HOMEBREW_COMPLETION_DIR]
    for d in alternatives:
        if os.path.exists(d) and os.path.isdir(d):
            return d
    return None


def install_script(path):
    pass


classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2.7',
]

config = {
    'name': 'aem-cmd',
    'version': __version__,
    'description': 'AEM Command line tools',
    'long_description': 'A set of tools to administer an Adobe AEM content management installation from the command line.',
    'license': 'MIT',
    'author': 'Björn Skoglund',
    'author_email': 'bjorn.skoglund@icloud.com',
    'url': 'https://github.com/bjorns/aem-cmd',
    'download_url': 'https://github.com/bjorns/aem-cmd',
    'classifiers': classifiers,

    # Build specs
    'install_requires': ['requests', 'lxml', 
                # test requirements
                'nose', 'mock', 'httmock'],
    'packages': ['acmd', 'acmd.tools'],
    'package_data': {'acmd': ['data/acmd.rc.template', 'data/acmd.bash_completion']},
    'scripts': ['bin/acmd'],

    # Installation
    'cmdclass': {'develop': InstallBashCompletionDevelop,
                 'install': InstallBashCompletion}
}

setup(**config)
