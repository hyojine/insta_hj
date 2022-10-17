from django.contrib import admin
from post.models import Post,Image

# Register your models here.
class Photoinline(admin.TabularInline):
    model = Image

class PostAdmin(admin.ModelAdmin):
    inlines = [Photoinline, ]

admin.site.register(Post, PostAdmin)