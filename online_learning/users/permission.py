from rest_framework.permissions import BasePermission


class ModeratorPermissionsClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff == True:
            return True
        return False

class IsOwnerPermissionsClass(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False