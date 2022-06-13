from rest_framework import permissions


class ReviewPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list']:
            return True
        elif view.action in ['create', 'retrieve', 'delete']:
            return request.user.is_authenticated
            # return True
        elif view.action in ['update', 'partial_update']:
            return False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_admin
        elif view.action in ['update', 'partial_update']:
            return False
        elif view.action == 'delete':
            return obj == request.user or request.user.is_admin
        else:
            return False
