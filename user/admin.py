from django.contrib import admin
# from .models import User

# admin.site.register(User)
# admin.site.register(User,UserAdmin) -> 원래 상태 (useradmin 임포트해야함)
# user랑 useradmin이 겹쳐서 useradmin 이 오버라이드해서 follow 필드가 사라짐
# 1) useradmin을 그대로 두려면 이걸 register 윗단에 추가해주면 되고 -> UserAdmin.fieldsets += (("custom", {"fields": ("following",)}), ) 
# 2) 아니면 위에 UserAdmin을 없애주면 됨
# 근데 유저어드민을 왜.. 내가 한거지..? 거북이반인가..?