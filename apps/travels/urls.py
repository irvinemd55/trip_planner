from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.travels, name="travels"),
    url(r'^destination/(?P<trip_id>\d+)', views.show, name="show"),
    url(r'^add', views.add, name="add"),
    url(r'^new', views.new, name="new"),
    url(r'^join/(?P<trip_id>\d+)', views.join, name="join"),
    url(r'^logout', views.logout, name="logout"),
]