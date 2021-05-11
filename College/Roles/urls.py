from django.urls import path
from Roles import views
from django.contrib.auth import views as ad

urlpatterns=[
path('',views.homepage,name='home'),
path('lg/',ad.LoginView.as_view(template_name='html/login.html'),name='lg'),
path('lgo/',ad.LogoutView.as_view(template_name='html/logout.html'),name='lgt'),
path('rg/',views.register,name='register')

]