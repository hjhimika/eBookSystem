from django.db import models

# Create your models here.

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings








class Permission(models.Model):
     name = models.CharField(max_length=255, unique=True)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
     updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

     class Meta:
          ordering = ('name',)

     def __str__(self):
          return self.name
     




class Role(models.Model):
     name = models.CharField(max_length=255, unique=True)
     permissions = models.ManyToManyField(Permission, blank=True)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

     updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
     
     class Meta:
          ordering = ('name',)

     def __str__(self):
          return self.name
     




class UserManager(BaseUserManager):
     def create_user(self, fullname, email, password=None):
          """
          Creates and saves a User with the given email, date of
          birth and password.
          """
          if not email:
               raise ValueError('Users must have an email address')

          user = self.model(
               fullname= fullname,
               email=self.normalize_email(email),
            
          )

          user.set_password(password)
          user.save(using=self._db)
          return user

     def create_superuser(self, fullname, email, password=None):
          """
          Creates and saves a superuser with the given email, date of
          birth and password.
          """
          user = self.create_user(
               email= email,
            
               password=password,
               fullname= fullname,
             
          )
          user.is_admin = True
          user.save(using=self._db)
          return user
     
 



class User(AbstractBaseUser):

     class Status(models.TextChoices):
          APPROVED = 'approve', _('Approve')
          NOT_APPROVED = 'not_approved', _('Not Approved')
         
     fullname = models.CharField(max_length=100,null=True, blank=True)
     password = models.CharField()
     username = models.CharField(max_length=100, null=True, blank=True, unique=True)
     email = models.EmailField(verbose_name='email address', max_length=255, null=True, blank=True, unique=True)
     status = models.CharField(max_length=16, choices=Status.choices, default=Status.NOT_APPROVED, null=True, blank=True)
  
     is_active = models.BooleanField(default=True)
     is_admin = models.BooleanField(default=False)

     role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
 
     created_at = models.DateTimeField(auto_now_add=True, null=True,  blank=True)
     updated_at = models.DateTimeField(auto_now=True, null=True,  blank=True)

     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
     updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

     objects = UserManager()

     USERNAME_FIELD = 'username'
     REQUIRED_FIELDS = ['fullname', 'gender']

     class Meta:
          ordering = ('-id',)

     def __str__(self):
          return self.email
