from django.urls import path
from apps.posts import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('posts/<slug>/', views.topic_posts, name='topic_posts'),
    path('posts/<int:pk>/<slug>/', views.post_detail, name='post_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
