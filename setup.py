try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='securepass',
    version='0.3.7',
    author="Giuseppe Paterno'",
    author_email='gpaterno@gpaterno.com',
    packages=['securepass'],
    scripts=['bin/sp-app-add','bin/sp-group-member','bin/sp-radius-mod','bin/sp-user-passwd','bin/sp-app-del','bin/sp-radius-add','bin/sp-user-add','bin/sp-user-provision', 'bin/sp-app-info','bin/sp-radius-del','bin/sp-user-auth','bin/sp-user-xattrs', 'bin/sp-app-mod','bin/sp-radius-info','bin/sp-user-del','bin/sp-users','bin/sp-apps','bin/sp-radius-list','bin/sp-user-info', 'bin/sp-user-mod', 'bin/sp-logs'],
    url='https://github.com/garlsecurity/securepass-tools',
    license='LICENSE.txt',
    description='SecurePass tools',
    long_description=open('README.txt').read(),
    install_requires=[
        "pycurl >= 7.19.0",
    ],
)

