from rest_framework import serializers
from rest_api import models


# class HelloSerializer(serializers.Serializer):
#     ''' Serializa un campo para nuestra APIView '''
#     name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    ''' Serializa un Objeto de Perfil de Usuario '''

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        ''' Crea y devuelve un nuevo usuario '''
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):
        ''' Actualiza la Cuenta de un Usuario '''
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)


# class ProfileFeedItemSerializer(serializers.ModelSerializer):
#     ''' Serializador de Profile Users '''

#     class Meta:
#         model = models.ProfileFeedItem
#         fields = ('id', 'user_profile', 'status_text', 'created_on')
#         extra_kwargs = {'user_profile': {'read_only': True}}


class WebsiteVisitCountSerializer(serializers.ModelSerializer):
    ''' Serializador de Website Visit Count '''

    class Meta:
        model = models.WebsiteVisitCount
        fields = ('page_id', 'webpage', 'visits', 'is_active')

    def create(self, validated_data):
        ''' Crea y devuelve un nuevo Website Visit Count '''
        print(validated_data)
        page = models.WebsiteVisitCount.objects.create(
            webpage = validated_data['webpage'],
        )
        return page
    
    def update(self, instance, validated_data):
        ''' Actualiza la Instancia del Website Visit Count '''
        webpage   = validated_data.get('webpage')
        visits    = validated_data.get('visits')
        is_active = validated_data.get('is_active')
        if webpage:
            instance.webpage = webpage
        if is_active.__class__ == bool:
            instance.is_active = is_active
        if visits.__class__ == int:
            instance.visits = visits
        elif not webpage and not is_active.__class__ == bool:
            instance.visits += 1
        instance.save()
        return instance
