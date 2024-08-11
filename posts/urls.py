from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('create',views.post_create , name='create'),
    path('feed', views.feed, name='feed'),

]