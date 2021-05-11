from django import forms
from Roles.models import User
from django.contrib.auth.forms import UserCreationForm
class RegForm(UserCreationForm):
	class Meta:
		model= User
		fields = '__all__'
