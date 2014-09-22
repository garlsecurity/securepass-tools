from distutils.core import setup

setup(
    name='SecurePass',
    version='0.1.0',
    author="Giuseppe Paterno'",
    author_email='gpaterno@gpaterno.com',
    packages=['securepass'],
    scripts=['bin/sp-app-add.py','bin/sp-group-member.py','bin/sp-radius-mod.py','bin/sp-user-passwd.py','bin/sp-app-del.py','bin/sp-radius-add.py','bin/sp-user-add.py','bin/sp-user-provision.py', 'bin/sp-app-info.py','bin/sp-radius-del.py','bin/sp-user-auth.py','bin/sp-user-xattrs.py', 'bin/sp-app-mod.py','bin/sp-radius-info.py','bin/sp-user-del.py','bin/sp-users.py','bin/sp-apps.py','bin/sp-radius-list.py','bin/sp-user-info.py'], 
    url='https://github.com/garlsecurity/securepass-tools',
    license='LICENSE.txt',
    description='SecurePass tools',
    long_description=open('README.txt').read(),
    install_requires=[
        "pycurl >= 7.19.0",
    ],
)

