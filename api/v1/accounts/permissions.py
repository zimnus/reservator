from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    message = 'You are already authenticated. Please log out to try again'
    """
    Non authenticated profile only
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
