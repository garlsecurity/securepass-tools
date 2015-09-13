import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def get_version_from_package(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)

main_package = 'securepass'

setup(
    name=main_package,
    version=get_version_from_package(main_package),
    author="Giuseppe Paterno'",
    author_email='gpaterno@gpaterno.com',
    packages=[main_package],
    scripts=['bin/sp-app-add','bin/sp-group-member','bin/sp-radius-mod','bin/sp-user-passwd','bin/sp-app-del','bin/sp-radius-add','bin/sp-user-add','bin/sp-user-provision', 'bin/sp-app-info','bin/sp-radius-del','bin/sp-user-auth','bin/sp-user-xattrs', 'bin/sp-app-mod','bin/sp-radius-info','bin/sp-user-del','bin/sp-users','bin/sp-apps','bin/sp-radius-list','bin/sp-user-info', 'bin/sp-user-mod', 'bin/sp-logs', 'bin/sp-realm-xattrs', 'bin/sp-sshkey', 'bin/sp-config'],
    url='https://github.com/garlsecurity/securepass-tools',
    license='LICENSE.txt',
    description='SecurePass tools',
    long_description=open('README.txt').read(),
    install_requires=[
        "pycurl >= 7.19.0",
    ],
)

