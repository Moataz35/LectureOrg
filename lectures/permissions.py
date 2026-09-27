from rest_framework.permissions import BasePermission
from authentication.models import Role

class IsAuthenticatedAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.ADMIN
    
class IsAuthenticatedProfessor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.PROFESSOR
