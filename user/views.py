from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('password_check')
        # print(username,password,passwordcheck)
        if password==passwordcheck:
            User.objects.create_user(username=username,password=password)
            return HttpResponse('회원가입성공')
        else:
            return HttpResponse('비밀번호를 확인해주세요')
    else:
        return HttpResponse('허용되지 않은 메소드입니다')

def login(request):
    return  HttpResponse('로그인페이지')