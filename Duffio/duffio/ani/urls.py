import profile
from django import views
from django.urls import path
from . import views

app_name = 'ani'

urlpatterns = [
    path('', views.top, name="top"),
    path('profile/', views.profile, name="profile"),
    path('diary/', views.diary, name="diary"),
    path('diary/add/', views.add, name="add"),
    path('album/', views.album, name="album"),
    path('fortune/', views.fortune, name="fortune"), # ページを増やしたいときはまずここでurlを追加する
]