from rest_framework.permissions import BasePermission
from authentication.models import Role

class IsAuthenticatedAdminOrProf(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in (Role.PROFESSOR, Role.ADMIN)

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user
