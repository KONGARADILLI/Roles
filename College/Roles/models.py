from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	r= [(1,'student'),(2,'teacher'),(3,'hod'),(4,'principal'),(0,'guest')]
	age= models.IntegerField(null=True)
	phonenu=models.IntegerField(null=True)
	rl=models.IntegerField(choices=r,default=0)
