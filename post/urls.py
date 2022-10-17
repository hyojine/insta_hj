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
    path('comment/create/<int:id>/',views.create_comment, name='create_comment'),
    path('comment/delete/<int:id>/',views.delete_comment, name='delete_comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)