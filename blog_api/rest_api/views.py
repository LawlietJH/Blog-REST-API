from rest_framework import filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_api import serializers, models, permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    ''' Crea y Actualiza Perfiles '''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnProfile,
        IsAuthenticated,
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    ''' Crea Tokens de Autenticación de Usuario '''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class WebsiteVisitCountViewSet(viewsets.ModelViewSet):
    ''' Maneja el Crear, Leer y Actualizar el Website Visit Count '''
    serializer_class = serializers.WebsiteVisitCountSerializer
    queryset = models.WebsiteVisitCount.objects.all()
    permission_classes = (
        permissions.UpdateWebsiteVisitCount,
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('page_id', 'webpage',)
