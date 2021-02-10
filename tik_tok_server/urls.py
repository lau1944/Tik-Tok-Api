
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('api/videos/', views.downloadVideos, name='videos'),
    path('api/trend/', views.trend, name='trend'),
    path('api/videoInfo/', views.getVideoById, name='videoInfo'),
    path('api/tiktok/', views.getTikTok, name='tiktok'),
    path('api/sound', views.getSound, name='sound'),
    path('api/user', views.getUserByName, name='user'),
    path('api/hashtag', views.getHashTag, name='hashtag'),
    path('api/discover/music', views.discoverMusic, name='music'),
    path('api/discover/hashtags', views.discoverHashtags, name='hashtags'),
]
