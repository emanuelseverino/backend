from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from usuarios.api.viewsets import UsuarioViewSet, CriarUsuarioViewSet

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('cadastro', CriarUsuarioViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('core.urls')),
                  path('', include(router.urls)),
                  path('login/', obtain_auth_token),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
