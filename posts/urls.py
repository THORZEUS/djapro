#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      EjemploJuan
#
# Created:     14/04/2018
# Copyright:   (c) EjemploJuan 2018
# Licence:     <your licence>
#--------------------------------------------------------------
from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')


];