# Django SecurePass APIs authentication backend
#
# This code is released under GPLv2
#
# (c) 2013 Giuseppe Paterno' (gpaterno@gpaterno.com)
#          GARL Sagl (www.garl.ch)
#

from . import securepass
from django.conf import settings
from django.contrib.auth.models import User


class SecurePassAuthBackend(object):

    """ SecurePass' core authentication backend
    Settings:
        SP_APP_ID          -> SecurePass APP ID
        SP_APP_SECRET      -> SecurePass APP Secret
        SP_ENDPOINT        -> API endpoint
        SP_AUTOCREATE_USER -> True/False, set if you want automatic creation
                              of user
        SP_REALM           -> SecurePass realm
    """

    # Actual auth
    def authenticate(self, username, password):

        endpoint = getattr(
            settings, 'SP_ENDPOINT', 'https://beta.secure-pass.net')
        autocreate = getattr(settings, 'SP_AUTOCREATE_USER', True)

        sp_handle = securepass.SecurePass(
            app_id=getattr(settings, 'SP_APP_ID', ''),
            app_secret=getattr(settings, 'SP_APP_SECRET', ''),
            endpoint=endpoint)

        # Add realm
        if '@' not in username:
            realm = getattr(settings, 'SP_REALM', 'login.farm')
            username = '{0}@{1}'.format(username, realm)

        if sp_handle.user_auth(user=username, secret=password):
            try:
                mapping = User.objects.get(username=username)

            except User.DoesNotExist:
                # user will have an "unusable" password
                if autocreate:
                    mapping = User.objects.create_user(username, '')
                    mapping.save()
                else:
                    return None

            try:
                myuser = sp_handle.user_info(user=username)

                mapping.first_name = myuser['name']
                mapping.last_name = myuser['surname']
                mapping.is_active = myuser['enabled']
                mapping.email = myuser['email']

                mapping.save()
            except:
                return None

            return mapping

        else:
            return None

    def get_user(self, user_id):
        """Retrieve the user's entry in the User model if it exists"""

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
