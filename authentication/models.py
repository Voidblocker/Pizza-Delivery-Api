from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import pgettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField



class CustomUserManager(BaseUserManager):

    def create_user(self, email, password , **extra_fields):
        if not email:
            raise ValueError(_("Email Should be Provided"))
        
        email = self.normalize_email(email)

        new_user = self.model(email=email, **extra_fields)

        new_user.set_password(password)

        new_user.save()

        return new_user

    def create_super_user(self, email, password, ** extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superUser', True)
        extra_fields.setdefault('is_active', True)

        for x in ['is_staff','is_superUser','is_active']:
            if extra_fields.get(f'{x}') is not True:
                raise ValueError(_(f"{x} must be set as True"))
            pass

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    phone_number = PhoneNumberField(blank=False, unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return self.email
    


