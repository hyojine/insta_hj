# from email import contentmanager
# from turtle import title
from pdb import post_mortem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Post, Image, Comment


# Create your views here.
def main(request):
    posts = Post.objects.all().order_by('-created_at') # 다 보여줄거니까 걍 다 가져오면 됨 일일이 저장 안해도됨
    context = {
        "posts":posts
    }
    return render(request, 'main.html', context)

def create_post(request):
    if request.method == 'GET':
        return render(request,'create_post.html')
    elif request.method =='POST':
        post = Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.user = request.user
        post.save()
        # Post.objects.create(title=title, content=content, user=user)
        print(request.FILES)
        for img in request.FILES.getlist('image'):
            i=Image()
            i.post=post
            i.image = img
            i.save()
        return redirect('post:detail',post_id=post.id)

def detail(request,post_id):
    # post = Post.objects.get(id=post_id) # do not exist error를 404 error로 바꿔줌 
    post = get_object_or_404(Post,id=post_id)
    context={'post':post}
    return render(request,'detail.html',context)

@login_required
def update(request,post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post,id=post_id)
        context={'post':post}
        return render(request,'update.html',context)
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post:main')

@login_required
def delete(request,post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')

# comment
@login_required
def create_comment(request,post_id):
    if request.method == 'GET':
        comment = get_object_or_404(Comment,id=post_id)
        context={'comments':comment}
        return render(request,'detail.html',context)
    elif request.method =='POST':
        comment = request.POST.get('comment')
        user = request.user
        Comment.objects.create(comment=comment, user=user)
        return redirect('post:detail')


@login_required
def delete_comment(request,post_id):
    comment=Post.objects.get(id=post_id)
    comment.delete()
    return redirect('post:detail')