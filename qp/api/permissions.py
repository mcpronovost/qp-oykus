from rest_framework.permissions import BasePermission


class qpIsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users with profile.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.profile and request.user.is_authenticated)
    
    # retrieve, update, delete
    # def has_object_permission(self, request, view, obj):
    #    return False
