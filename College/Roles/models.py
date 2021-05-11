from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	r= [(1,'student'),(2,'teacher'),(3,'hod'),(4,'principal'),(0,'guest')]
	age= models.IntegerField(null=True)
	phonenu=models.IntegerField(null=True)
	rl=models.IntegerField(choices=r,default=0)

class RoleRest(models.Model):
	t=[(1,'student'),(2,'teacher')]
	uname= models.CharField(max_length=30)
	roletype = models.PositiveIntegerField(choices=t)
	prf = models.CharField(max_length=250)
	is_checked=models.BooleanField(default=0)
	uid= models.OneToOneField(User,on_delete=models.CASCADE)