from django.conf.urls import url
from django.urls import path 

from . import views

app_name = 'appsec'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^appsec/index/*$', views.index, name='index'),
    url(r'^appsec/spellchecker/*$', views.spellchecker, name='spellchecker'),
    url(r'^appsec/imageresizer/*$', views.imageresizer, name='imageresizer'),
]
 
