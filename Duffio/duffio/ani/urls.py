from django import views
from django.urls import path
from . import views

app_name = 'ani'

urlpatterns = [
    path('', views.index, name="index"), # ページを増やしたいときはまずここでurlを追加する
]