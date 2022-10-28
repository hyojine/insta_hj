# from pdb import post_mortem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Post, Image, Comment

# 메인페이지
def main(request):
    posts = Post.objects.all().order_by('-created_at') # 다 보여줄거니까 걍 다 가져오면 됨 일일이 저장 안해도됨
    context = {
        "posts":posts
    }
    return render(request, 'main.html', context)

# 게시글 작성
def create_post(request):
    if request.method == 'GET':
        return render(request,'create_post.html')
    elif request.method =='POST':
        post = Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.author = request.user
        post.save()
        # Post.objects.create(title=title, content=content, user=user)
        print(request.FILES)
        for img in request.FILES.getlist('image'):
            i=Image()
            i.post=post
            i.image = img
            i.save()
        return redirect('post:detail',post_id=post.id)

# 게시글 상세 페이지
def detail(request,post_id):
    if request.method == 'GET':
        # post = Post.objects.get(id=post_id) # do not exist error를 404 error로 바꿔줌 
        post = get_object_or_404(Post,id=post_id)
        comment = Comment.objects.filter(post_id=post_id) #filter vs get
        context={'post':post,'comments':comment}
        return render(request,'detail.html',context)

# 게시글 수정
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

# 게시글 삭제
@login_required
def delete(request,post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')

# 댓글 생성
@login_required
def create_comment(request,post_id):
    print(request.method)
    if request.method =='POST':
        com = Comment()
        com.post=Post.objects.get(id=post_id)
        com.comment = request.POST.get('comment','')
        com.user = request.user
        com.save()
        # print('ssssssssssssaveeeeeeeeeeee') #save 확인용
        # comment = request.POST.get('comment')
        # user = request.user
        # Comment.objects.create(comment=comment, user=user)
        return redirect('post:detail',post_id)

# 댓글 수정
@login_required
def update_comment(request,comment_id):
    if request.method == 'GET':
        comment = get_object_or_404(Comment,id=comment_id)
        context={'comment':comment}
        return render(request, 'comments/update_comment.html', context=context)
    elif request.method =='POST':
        com = Comment.objects.get(id=comment_id) #이미 있는걸 가져와서 바꾸는 것만 바꿔야 null값이 없구나
        com.comment = request.POST.get('comment','')
        com.save() #NOT NULL constraint failed: post_comment.post_id
        postid=com.post_id
        print('ssssssssssssaveeeeeeeeeeee')
        return redirect('post:detail',postid)

# 댓글 삭제
@login_required
def delete_comment(request,comment_id):
    comment=Comment.objects.get(id=comment_id)
    postid=comment.post_id
    comment.delete()
    return redirect('post:detail', postid)

# 좋아요
def likes(request, post_id):
    if request.method == 'POST':
       post = Post.objects.get(id=post_id)
    if post.like_authors.filter(id=request.user.id).exists():
       post.like_authors.remove(request.user)
    else:
        post.like_authors.add(request.user)
    return redirect('post:detail',post_id)

# 좋아요 누른 글 목록
@login_required(login_url='user:sign_in')
def likes_list(request, post_id):
    pass
