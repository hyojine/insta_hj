from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# 이 파일이 있는 경로에 있는 models.py 여기선 user앱의 models.py

admin.site.register(User, UserAdmin)