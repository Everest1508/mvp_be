from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(models.Model):   
    name     = models.CharField(max_length=255)
    email    = models.EmailField(unique=True)
    phone    = models.CharField(max_length=15, unique=True)
    age      = models.PositiveIntegerField()
    college  = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'age', 'college']

    def __str__(self):
        return self.name

class College(models.Model):
    title = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
class Games(models.Model):
    title = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title