from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = '''
        You must be owner of this content to change
    '''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
