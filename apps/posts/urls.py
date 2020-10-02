from django.urls import path
from apps.posts import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/v1/posts/', views.PostList.as_view()),
    path('api/v1/posts/<int:pk>/', views.PostDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
