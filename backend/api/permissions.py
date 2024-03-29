from rest_framework import permissions


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


class IsUnauthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            return not (request.user and request.user.is_authenticated)
        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id


class AuthenticatedUserCanReadAndModify(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.method != 'POST'
        else:
            return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
    

class NoModify(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH']:
            return False
        return True
