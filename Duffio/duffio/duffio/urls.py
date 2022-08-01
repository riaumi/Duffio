from django.contrib import admin
from django.urls import path, include #includeを追加、aniアプリのurlを取り込む

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ani/', include('ani.urls')), #ani.urlを追加
]
