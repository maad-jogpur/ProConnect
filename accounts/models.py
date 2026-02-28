from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,last_name,password=None):
        if not username:
            raise ValueError("User must have a username")
        if not email:
            raise ValueError("User must have an email")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,first_name,last_name,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    ROLE = (
        ('Job Seeker','Job Seeker'),
        ('Job Recruiter','Job Recruiter')
    )
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100 )
    last_name = models.CharField(max_length=100)
    role = models.CharField(choices=ROLE)
    phone_number = models.CharField(max_length=10)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


    REQUIRED_FIELDS = ['first_name','last_name','username']
    USERNAME_FIELD = 'email'

    objects = AccountManager()

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,add_label):
        return self.is_admin
