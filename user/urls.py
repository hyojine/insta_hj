from django.contrib import admin
from django.urls import path, include
from user import views
# 왜 .user 아니지?

app_name='user'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
]
