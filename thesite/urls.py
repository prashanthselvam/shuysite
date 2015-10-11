from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^fine_art/$', views.fine_art, name='fine_art'),
    url(r'^about/$', views.about, name='about'),
    url(r'^graphic_design/$', views.graphic_design, name='graphic_design'),
    url(r'^video/$', views.video, name='video'),
    url(r'^contact/$', views.contact_form, name='contact_form'),
]