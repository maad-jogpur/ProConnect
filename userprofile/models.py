from django.db import models
from accounts.models import Account
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_pic',blank=True)

    skills = models.CharField(max_length=100, blank=True)
    experience = models.TextField(blank=True)

    company_name = models.CharField(max_length=200,blank=True)
    company_description = models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return f"{self.user.first_name}"
    
