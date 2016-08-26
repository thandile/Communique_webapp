from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """
    Custom permission to permit only active users access.
    """
    def has_permission(self, request, view):
        """
        Checks whether the user making the request is an active user.
        """
        return request.user.is_active


class IsSuperUser(permissions.BasePermission):
    """
    Custom permission to permit only superuser access.
    """
    def has_permission(self, request, view):
        """
        Checks whether the user making the request is a superuser.
        """
        return request.user.is_superuser


class IsProfileOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owner a profile of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        return str(obj.pk) == str(request.user.pk)