from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from django.contrib.auth.models import User as Users
from django.contrib.auth import authenticate, login as loginsession
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
            return render(request,'login.html')
        else:
            return HttpResponse('비밀번호를 확인해주세요')
    else:
        return HttpResponse('허용되지 않은 메소드입니다')

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            loginsession(request,user)
            return redirect('user:profile',username=username)
        else:
            return  redirect('/login')

# 프로필 페이지
@login_required
def profile(request, username):
    content = get_object_or_404(User, username=username)
    # content = User.objects.get(username=username)
    context={"user":content}
    return render(request,'profile.html',context)

# 팔로우
@login_required
def userlist(request):
    if request.method == 'GET':
        user_list = User.objects.all().exclude(username=request.user.username)
        return render(request,'userlist.html',{'user_list':user_list})

@login_required
def follow(request, id):
    me = request.user
    clicker = User.objects.get(id=id)
    if me in clicker.following.all():
        clicker.following.remove(request.user)
    else:
        clicker.following.add(request.user)
    return redirect('/userlist/')