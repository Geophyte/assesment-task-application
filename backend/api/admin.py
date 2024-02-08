from django.contrib import admin
from .models import Category, Task, CustomUser, Comment


admin.site.register(Category)
admin.site.register(Task)
admin.site.register(CustomUser)
admin.site.register(Comment)
