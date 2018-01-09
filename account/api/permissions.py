from rest_framework import permissions


class BlacklistPermissions(permissions.BasePermission):
    """
    Check blacklist IP
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklist = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklist


class AnonPermissionOnly(permissions.BasePermission):
    message = 'You are4 already authenticated. Please log out to try again'
    """
    Non authenticated user only
    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated()

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "You must be the owner of this content to change"
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user