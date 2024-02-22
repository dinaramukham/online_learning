from rest_framework.permissions import BasePermission

class IsOwnerPermissionsClass(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.payment.user:
            return True
        return False