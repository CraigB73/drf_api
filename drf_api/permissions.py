from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS: #return true if user has permission
            return True
        return obj.owner == request.user #return true only if post belongs to user