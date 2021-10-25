from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import *
from rest_framework.mixins import *

from usuarios.api.serializers import *

Usuario = get_user_model()


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.queryset.get(email=self.request.user.email)


class CriarUsuarioViewSet(GenericViewSet, CreateModelMixin):
    queryset = Usuario.objects.all()
    serializer_class = CriarUsuarioSerializer

