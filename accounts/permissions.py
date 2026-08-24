from rest_framework.permissions import BasePermission, SAFE_METHODS


def get_user_role(user):
    if not user or not user.is_authenticated:
        return None
    if user.is_superuser:
        return 'admin'
    profile = getattr(user, 'profile', None)
    if profile is None:
        return None
    return profile.role


class IsAuthenticatedActive(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if not user.is_active:
            return False
        profile = getattr(user, 'profile', None)
        if profile is not None and not profile.is_active_user:
            return False
        return True


class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return get_user_role(request.user) == 'admin'


class IsOperatorOrAdmin(BasePermission):
    """Write access for operator/admin; read for any authenticated role."""

    def has_permission(self, request, view):
        role = get_user_role(request.user)
        if role is None:
            return False
        if request.method in SAFE_METHODS:
            return role in ('admin', 'operator', 'viewer')
        return role in ('admin', 'operator')


class ReadOnlyOrOperator(BasePermission):
    def has_permission(self, request, view):
        role = get_user_role(request.user)
        if role is None:
            return False
        if request.method in SAFE_METHODS:
            return True
        return role in ('admin', 'operator')
