from django.db import models

# Create your models here.



class Login(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=8)
    cmpassword=models.CharField(max_length=8)
    

    def __str__(self):
        return self.email


class URL(models.Model):
    orginalurl= models.URLField()
    shorturl=models.CharField(max_length=50,unique=True)