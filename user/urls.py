from django.contrib import admin
from django.urls import path, include
from user import views
# 왜 .user 아니지?

app_name='user'

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('userlist/',views.userlist,name='userlist'),
    path('follow/<int:id>/',views.follow,name='follow'),
    path('<str:username>/',views.profile, name='profile'),
    # not found 'userlist'
    # 프로필 함수 실행 url이 문자열이라서 저 경로가 자꾸 먼저 실행되어버림(순서)
    # 그래서 일단은 가장 아래로 내려줬지만..
    # 앞으로는 url만들 때 꼭 앞에 app 이름 붙여줘야지.. 자꾸 불상사가 발생함

]
