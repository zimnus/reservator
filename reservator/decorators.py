from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


# Only enterprise manager permission
def manager_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/login/'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.manager,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# Only client access
def client_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/login/'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.client,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
