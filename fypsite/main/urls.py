from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import login
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'main'
urlpatterns = [
    path('', views.index, name="index"),

     path('sign',views.sign, name="sign"),
      #path('login', views.login, name="login")
     # url(r'^login/$', login, {'template_name' : 'login.html'})
    #url(r'^login/$', auth_views.login, name='login'),
    url( r'^login/$',auth_views.LoginView.as_view(template_name="main/login.html"), name="login"),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
 ]
