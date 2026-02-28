from django.db import models
from accounts.models import Account
# Create your models here.

class Job(models.Model):
    
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    requirement = models.TextField(max_length=500,blank = True)
    job_location = models.CharField(max_length=100)
    job_salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


 