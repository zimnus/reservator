from django.contrib.auth import get_user_model, authenticate


class AdminBackend(object):
    def authenticate(self, username, request):
        if not request.user.has_perm('auth.change'):
            return None
        try:
            user = get_user_model().objects.get(username=username)
            if user.is_superuser:
                return None
            return user
        except get_user_model().DoesNotExist:
            return None


class EmailBackend(object):
    def authenticate(self, email, password):
        try:
            user = get_user_model().objects.filter(email__iexact=email, is_active=True)[0]
            return authenticate(username=user.username, password=password)
        except IndexError:
            return None

    def get_user(self, user_id):
        user_set = get_user_model().objects.filter(pk=user_id)
        if user_set.exists():
            return user_set[0]
        return None
