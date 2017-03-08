from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index$', views.index, name='index'),
    url(r'^contactus$', views.contactus, name='contactus'),
    url(r'^aboutus$', views.aboutus, name='aboutus'),
    url(r'^extra$', views.extra, name='extra'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^message$', views.message, name='message'),
    url(r'^chat$', views.chat, name='chat'),
    url(r'^tendar$', views.tendar, name='tendar'),
    url(r'^suggestion$', views.suggestion, name='suggestion'),
    url(r'^complain$', views.complain, name='complain'),
]