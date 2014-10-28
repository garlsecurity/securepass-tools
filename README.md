SecurePass public CLI tools
===========================

The tools for accessing SecurePass from command line.
Uses the SecurePass public APIs to manage.

More information on the APIs here:
https://beta.secure-pass.net/

Note: For OS X, ensure you have the following while compiling pycurl:
export PYCURL_SSL_LIBRARY=openssl

This program is released under GPLv2
See LICENSE file for details


Configuration file
==================

Configuration *only for cli tools* should be placed in:
/etc/securepass.conf /usr/local/etc/securepass.conf or securepass.conf in current local directory.
For an example check out securepass.conf.example



Django Backend
==============

The Django backend for SecurePass RESTful APIs authenticated and sync information from
SecurePass (first name, last name, e-mail) each time, so that information is up to date.
Also state of enable/disable is reflected in is_active, so that the user is automatically disabled.

Note: we do not handle staff at this time. For future that will be reflected into groups.

The following settings have to be put into settings.py

Required:
```
SP_APP_ID = <<SecurePass APP ID>>
SP_APP_SECRET = <<SecurePass APP Secret>>
```

Optional:
```
SP_ENDPOINT = <<endpoint if different from default>>
SP_AUTOCREATE_USER = <<True/False, autocreate user if not in database>>
```

Put securepass-tools in installed apps
```
INSTALLED_APPS += (
    'securepass-tools',
)
```

Put the django authentication backend
```
AUTHENTICATION_BACKENDS = (
    'securepass-tools.djangoauth.SecurePassAuthBackend',
)
```
