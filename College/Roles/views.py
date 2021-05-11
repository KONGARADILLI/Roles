from django.shortcuts import render
from Roles.forms import RegForm
# Create your views here.
def homepage(request):
	return render(request,'html/home.html')

def register(request):
	q=RegForm()
	return render(request,'html/register.html')