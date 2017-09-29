from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^main', views.index, name="index"),
    url(r'^authenticate', views.authenticate, name="authenticate"),
    url(r'^register_user', views.register_user, name="register_user"),
    url(r'^logout', views.logout, name="logout"),
 ]