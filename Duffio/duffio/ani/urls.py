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
# <int:pk>というのは、それぞれの記事に紐づいている主キーという意味
# 一覧や追加ページはそれぞれの記事に紐づいていないので不要
    path('diary/update/<int:pk>', views.update, name="update"),
    path('diary/delete/<int:pk>', views.update, name="delete"),
    path('diary/detail/<int:pk>', views.update, name="detail"),
    path('album/', views.album, name="album"),
    path('fortune/', views.fortune, name="fortune"), # ページを増やしたいときはまずここでurlを追加する
]