from rest_framework import permissions
from django.dispatch import receiver


class UpdateOwnProfile(permissions.BasePermission):
    ''' Permite al usuario editar su propio perfil '''

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS \
        or request.user.is_superuser:
            return True
        
        return False

    def has_object_permission(self, request, view, obj):
        ''' Verifica si se intenta modificar el perfil propio '''
        
        if request.method in permissions.SAFE_METHODS \
        or request.user.is_superuser:
            return True
        
        return obj.id == request.user.id


class UpdateWebsiteVisitCount(permissions.BasePermission):
    ''' Permite al Super Usuario Editar los contadores de visitas '''

    def has_permission(self, request, view):
        ''' Verifica si se intenta modificar el contador de visitas '''
        if request.method in permissions.SAFE_METHODS \
        or request.user.is_superuser:
            return True
        
        return False

    def has_object_permission(self, request, view, obj):
        ''' Verifica si se intenta modificar el contador de visitas '''
        if request.method in permissions.SAFE_METHODS \
        or request.user.is_superuser:
            return True
        
        return False
