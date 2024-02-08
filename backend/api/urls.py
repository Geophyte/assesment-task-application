from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views.category import CategoryViewSet
from .views.task import TaskViewSet
from .views.user import UserViewSet, login_user, logout_user, register
from .views.comment import CommentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('comments/user/<int:user_id>/', CommentViewSet.as_view({'get': 'user_comments'}), name='user-comments'),
    path('comments/task/<int:task_id>/', CommentViewSet.as_view({'get': 'task_comments'}), name='task-comments'),
    path('comments/user/<int:user_id>/task/<int:task_id>/', CommentViewSet.as_view({'get': 'user_task_comments'}), name='user-task-comments'),
    path('comments/task/<int:task_id>/user/<int:user_id>/', CommentViewSet.as_view({'get': 'user_task_comments'}), name='user-task-comments'),
]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
