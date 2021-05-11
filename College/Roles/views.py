from django.shortcuts import render,redirect
from Roles.forms import RegForm
# Create your views here.
def homepage(request):
	return render(request,'html/home.html')

def register(request):
	if request.method == "POST":
		q = RegForm(request.POST)
		if q.is_valid():
			q.save()
			return redirect('/lg')
	q=RegForm()
	return render(request,'html/register.html',{'y':q})