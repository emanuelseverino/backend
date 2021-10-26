from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        usuario = self.model(email=email, username=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Staff precisa ter is_staff=True')
        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='usuarios', blank=True, null=True)
    email = models.EmailField('E-mail', unique=True)
    celular = models.CharField('Celular', unique=True, max_length=30)
    cidade = models.CharField('Cidade', max_length=200, blank=True, null=True)
    is_staff = models.BooleanField('Membro da Equipe', default=False)
    instagram = models.CharField('Instagram', unique=True, max_length=30, blank=True, null=True)
    whatsapp = models.CharField('Whatsapp', unique=True, max_length=30, blank=True, null=True)
    facebook = models.CharField('Facebook', unique=True, max_length=30, blank=True, null=True)
    twitter = models.CharField('Twitter', unique=True, max_length=30, blank=True, null=True)
    latitude = models.CharField('Latitude', unique=True, max_length=30, blank=True, null=True)
    longitude = models.CharField('Longitude', unique=True, max_length=30, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'celular']

    def __str__(self):
        return self.email

    objects = UsuarioManager()
