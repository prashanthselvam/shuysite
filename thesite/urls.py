from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^fine_art/$', views.fine_art, name='fine_art'),
    url(r'^about/$', views.about, name='about'),
]