from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=20)
    sex=models.CharField(max_length=10)
    age=models.IntegerField()
    group=models.CharField(max_length=4)
    idpassword=models.CharField(max_length=19,unique=True)
