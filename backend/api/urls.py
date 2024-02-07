from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.category import CategoryViewSet
from .views.task import TaskViewSet
from .views.user_profile import UserProfileViewSet
from .views.comment import CommentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comments/user/<int:user_id>/', CommentViewSet.as_view({'get': 'user_comments'}), name='user-comments'),
    path('comments/task/<int:task_id>/', CommentViewSet.as_view({'get': 'task_comments'}), name='task-comments'),
    path('comments/user/<int:user_id>/task/<int:task_id>/', CommentViewSet.as_view({'get': 'user_task_comments'}), name='user-task-comments'),
    path('comments/task/<int:task_id>/user/<int:user_id>/', CommentViewSet.as_view({'get': 'user_task_comments'}), name='user-task-comments'),
]

urlpatterns += router.urls
