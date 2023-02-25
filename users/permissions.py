from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # GET의 경우에는 모두 가능하도록 하고, 다른 메소드의 경우에는 해당 유저가 일치한 경우에만 가능하도록 함
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
