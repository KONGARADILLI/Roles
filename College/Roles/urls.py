from django.urls import path
from Roles import views
from django.contrib.auth import views as ad

urlpatterns=[
path('',views.homepage,name='home'),
path('lg/',ad.LoginView.as_view(template_name='html/login.html'),name='lg'),
path('lgo/',ad.LogoutView.as_view(template_name='html/logout.html'),name='lgt'),
path('rg/',views.register,name='register'),
path('pf/',views.profile,name='prf'),
path('upf/',views.updateprofile,name='updatepf'),
path('per/',views.permissions,name='perm'),
path('rlrq',views.rolreq,name='rr'),
path('gvp/<int:k>/',views.giveper,name='gvpr'),
]