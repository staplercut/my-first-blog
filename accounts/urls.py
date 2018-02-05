from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from accounts.forms import LoginForm


urlpatterns = [
#(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),

    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),

]