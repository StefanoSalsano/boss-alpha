#to cutomizing authenticate backend

from django.conf import settings
from django.contrib.auth.models import User, check_password

class EmailAuthentication(object):
        def authenticate(self, username=None, password=None):
            login_valid = ( settings.ADMIN_LOGIN == email )
            pwd_valid = check_password( password, setting.ADMIN_PASSWORD )
            if login_valid and pwd_valid:
                try:
                    user = User.objects.get(email=username)
                except User.DoesNotExist:
                    user = User ( email=username, password= password )
                    user.is_active = True
                    user.save()
                return user
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

