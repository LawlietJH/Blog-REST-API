from pyexpat import model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_api import serializers, models, permissions


# class HelloAPIView(APIView):
#     ''' API View de Prueba '''
#     serializer_class = serializers.HelloSerializer

#     def get(self, request, format=None):
#         ''' Devuelve una lista de caracteristicas del APIView'''
#         an_apiview = [
#             'Usamos métodos HTTP como funciones (get, post, patch, put, delete)',
#             'Es similar a una vista tradicional de Django',
#             'Nos da el mayor control sobre la lógica de nuestra aplicación',
#             'Esta mapeado manualmente a los URLs',
#         ]

#         return Response({
#             'message': 'Hello',
#             'an_apiview': an_apiview 
#         })
    
#     def post(self, request):
#         ''' Crea un mensaje con nuestro nombre '''
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'hello {name}'
#             return Response({
#                 'message': message
#             })
#         else:
#             return Response(
#                 serializer.errors,
#                 status = status.HTTP_400_BAD_REQUEST
#             )

#     def put(self, request, pk=None):
#         ''' Actualiza un Objeto '''
#         return Response({
#             'method': 'PUT'
#         })

#     def patch(self, request, pk=None):
#         ''' Actualiza una parte de un Objeto '''
#         return Response({
#             'method': 'PATCH'
#         })

#     def delete(self, request, pk=None):
#         ''' Actualiza una parte de un Objeto '''
#         return Response({
#             'method': 'DELETE'
#         })


# class HelloViewSet(viewsets.ViewSet):
#     ''' Test API ViewSet '''
#     serializer_class = serializers.HelloSerializer

#     def list(self, request):
#         return Response({
#             'message': 'Hola!'
#         })
    
#     def create(self, request):

#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'hola {name}'
#             return Response({
#                 'message': message
#             })
#         else:
#             return Response(
#                 serializer.errors,
#                 status = status.HTTP_400_BAD_REQUEST
#             )
    
#     def retrieve(self, request, pk=None):
#         return Response({
#             'http_method': 'GET'
#         })
    
#     def update(self, request, pk=None):
#         return Response({
#             'http_method': 'PUT'
#         })
        
#     def partial_update(self, request, pk=None):
#         return Response({
#             'http_method': 'PATCH'
#         })
        
#     def destroy(self, request, pk=None):
#         return Response({
#             'http_method': 'DELETE'
#         })


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


# class UserProfileFeedViewSet(viewsets.ModelViewSet):
#     ''' Maneja el Crear, Leer y Actualizar el Profile Feed '''
#     authentication_classes = (TokenAuthentication,)
#     serializer_class = serializers.ProfileFeedItemSerializer
#     queryset = models.ProfileFeedItem.objects.all()
#     permission_classes = (
#         permissions.UpdateOwnStatus,
#         IsAuthenticated,
#     )

#     def perform_create(self, serializer):
#         ''' Setear al Perfil de Usuario para el Usuario que esta logeado '''
#         serializer.save(user_profile=self.request.user)


class WebsiteVisitCountViewSet(viewsets.ModelViewSet):
    ''' Maneja el Crear, Leer y Actualizar el Website Visit Count '''
    serializer_class = serializers.WebsiteVisitCountSerializer
    queryset = models.WebsiteVisitCount.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateWebsiteVisitCount,
        IsAuthenticated,
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('page_id', 'webpage',)
