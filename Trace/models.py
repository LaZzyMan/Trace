from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    usertype = models.CharField(max_length=10)

class User(models.Model):
    username = models.ForeignKey(Person,on_delete=models.CASCADE)
    SID = models.CharField(max_length=10)
    IDCardNum = models.CharField(max_length=20)
    realName = models.CharField(max_length=20)
    phoneNum = models.CharField(max_length=15)
