from rest_framework.permissions import BasePermission


class IsOwnerPermissionsClass(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsModer(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='модераторы').exists():
            return True
        return False
