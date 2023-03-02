from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email=None, username=None, password=None):
        if not email and not username:
            raise ValueError('Los usuarios deben tener una dirección de correo electrónico o un nombre de usuario')

        if email:
            email = self.normalize_email(email)
            email = email.lower()

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email=None, username=None, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_accounts',
        blank=True,
        verbose_name='grupos'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_accounts',
        blank=True,
        verbose_name='permisos de usuario'
    )

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_username(self):
        return self.username

    def __str__(self):
        return self.email or self.username
