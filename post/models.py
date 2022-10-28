from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='media/',default='insta/static/media/image.jpg')
    content = models.TextField(blank = True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 탈퇴할 때(user가 없어지면) 내가 쓴 글(post)을 모두 지우겠다
    like_authors = models.ManyToManyField(User, related_name='like_posts')
    # related_name 역참조
    def __str__(self):
        return str(self.title)

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

