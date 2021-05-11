from django import forms
from Roles.models import User,RoleRest
from django.contrib.auth.forms import UserCreationForm
class RegForm(UserCreationForm):
	password1= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2 ","placeholder":"Password"}))
	password2= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2 ","placeholder":"confirm Password"}))

	class Meta:
		model= User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
		}

class UpPrf(forms.ModelForm):
	class Meta:
		model= User
		fields = ["username","first_name","last_name","email","age","phonenu"]
		widgets = {
		"username":forms.TextInput(attrs={"class":"form-control","readonly":True}),

		"first_name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"First name"}),
		"last_name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Last name"}),
		"email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"Enter your email"}),
		"age":forms.NumberInput(attrs={"class":"form-control my-2","placeholder":"Enter your age"}),
		"phonenu":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Phone number"}),

		}

class RoleR(forms.ModelForm):
	class Meta:
		model = RoleRest
		fields= ["roletype","prf"]
		widgets={
		"uname":forms.TextInput(attrs={"class":"form-control","readonly":True}),

		"roletype":forms.Select(attrs = {"class": "form-control",}),
		"prf":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter proof"}),


		}

class RolUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","rl"]
		widgets={
		"username": forms.TextInput(attrs={"class":"form-control","readOnly":True,}),
		"rl":forms.Select(attrs={"class":"form-control"}),
		}
