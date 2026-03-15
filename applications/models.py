from django.db import models
from accounts.models import Account
from jobs.models import Job
# Create your models here.
 
class Application(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Selected','Selected'),
        ('Rejected','Rejected'),
    )
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resume")
    cover_letter = models.TextField(max_length=1000)
    status = models.CharField(choices=STATUS, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.job} - {self.user} "