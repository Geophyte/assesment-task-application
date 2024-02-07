from django.contrib import admin
from .models import Category, Task, UserProfile, Comment


admin.site.register(Category)
admin.site.register(Task)
admin.site.register(UserProfile)
admin.site.register(Comment)
