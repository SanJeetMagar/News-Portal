from rest_framework.permissions import BasePermission
from src.apps.auth.models import Role


class RolePermission(BasePermission):
    allowed_roles: list[str] = []

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in self.allowed_roles
        )


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.role in [Role.ADMIN, Role.SUPERADMIN]:
            return True
        return hasattr(obj, "advertiser") and obj.advertiser == request.user

class IsSuperAdmin(RolePermission):
    allowed_roles = [Role.SUPERADMIN]


class IsAdminOrSuperAdmin(RolePermission):
    allowed_roles = [Role.ADMIN, Role.SUPERADMIN]


class IsEditor(RolePermission):
    allowed_roles = [Role.EDITOR, Role.ADMIN, Role.SUPERADMIN]


class IsAdvertiser(RolePermission):
    allowed_roles = [Role.ADVERTISER, Role.ADMIN, Role.SUPERADMIN]


class IsAuthor(RolePermission):
    allowed_roles = [Role.AUTHOR, Role.EDITOR, Role.ADMIN, Role.SUPERADMIN]


class IsUser(RolePermission):
    allowed_roles = [Role.USER, Role.AUTHOR, Role.EDITOR, Role.ADVERTISER, Role.ADMIN, Role.SUPERADMIN]
