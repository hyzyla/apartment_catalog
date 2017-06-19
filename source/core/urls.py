from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<room_count>\d+)/', views.index),
    url(r'search', views.index)
]