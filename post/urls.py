from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

app_name='post' # 다른걸로 해도 상관없음

urlpatterns = [
    # post
    path('',views.main, name='main'),
    path('post/create/',views.create_post, name='create_post'),
    path('post/<int:post_id>/',views.detail, name='detail'),
    path('post/<int:post_id>/delete/',views.delete, name='delete'),
    path('post/<int:post_id>/update/',views.update, name='update'),
    
    # comment
    path('comment/create/<int:post_id>/',views.create_comment, name='create_comment'),
    path('comment/update/<int:comment_id>/',views.update_comment, name='update_comment'),
    path('comment/delete/<int:comment_id>/',views.delete_comment, name='delete_comment'),

    # like
    path('post/likes/<int:post_id>/', views.likes, name='likes'),
    # path('post/likes/list/<int:post_id>/', views.likes_list, name='like-list'),

    # #search
    # path('search/', views.search, name='search'),

    # #follow
    # path('post/followlist/<int:post_id>/', views.follow_list, name='follow-list'),
]


