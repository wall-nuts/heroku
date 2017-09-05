#coding:utf-8
from django.conf.urls import include, url

from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^db',views.db,name='db'),
	url(r'^book',views.book,name='book'),
	url(r'^blog',views.blog,name='blog'),
	url(r'^record', views.record, name='record'),
	url(r'^',views.index,name='home'),

]