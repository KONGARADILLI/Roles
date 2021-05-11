from django.shortcuts import render,redirect
from Roles.forms import RegForm,UpPrf,RoleR,RolUp
from django.contrib.auth.decorators import login_required
from Roles.models import User
# Create your views here.
@login_required
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

@login_required
def profile(request):
	return render(request,'html/profile.html')

@login_required
def updateprofile(request):
	if request.method== "POST":
		p=UpPrf(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/pf')
	p= UpPrf()
	return render(request,'html/updateprofile.html',{'e':p})

@login_required
def permissions(request):
	ty=User.objects.all()
	return render(request,'html/givepermissions.html',{'q':ty})

@login_required
def rolreq(request):
	if request.method== "POST":
		k =RoleR(request.POST)
		if k.is_valid():
			s=k.save(commit=False)
			s.uname= request.user.username
			s.uid_id= request.user.id
			s.save()
			return redirect('/pf')
	k=RoleR()
	return render(request,'html/rolreq.html',{'a':k})
@login_required
def giveper(request,k):
	r=User.objects.get(id=k)
	if request.method == "POST":
		k=RolUp(request.POST,instance=r)
		if k.is_valid():
			e=k.save(commit=False)
			e.save()
			return redirect('/per')
	k2= RolUp(instance=r)
	return render(request,'html/approvepermissions.html',{'y':k2})
