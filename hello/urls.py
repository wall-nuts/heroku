#coding:utf-8
from django.conf.urls import include, url

from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^',views.index,name='home'),
	url(r'^db',views.db,name='db'),
]