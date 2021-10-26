from django.contrib.auth import get_user_model
# from drf_extra_fields.fields import Base64ImageField
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import GenericViewSet

Usuario = get_user_model()


class UsuarioSerializer(ModelSerializer):
    foto = Base64ImageField(required=False)

    class Meta:
        model = Usuario
        fields = ['foto', 'first_name', 'last_name', 'email', 'celular', 'whatsapp', 'facebook', 'instagram', 'twitter',
                  'latitude',
                  'longitude']


class CriarUsuarioSerializer(ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'celular', 'email', 'password', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario(username=validated_data['email'], **validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario
