from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so GET, HEAD or OPTIONS are allowed.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only to owner
        return obj.owner == request.user
