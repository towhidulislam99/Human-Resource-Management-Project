from django.db import models
from role.models import Role

# Create your models here.

class User(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='media/', default='No images', null=True)
    

