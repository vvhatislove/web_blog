from django.urls import path, include, re_path

from blog.views import PostUpdateAPIView, PostDeleteAPIView, PostCreateAPIView, PostListAPIView, PostDetailAPIView, \
    CategoryDetailAPIView, CategoryListAPIView, CategoryCreateAPIView, CategoryDeleteAPIView, CategoryUpdateAPIView

urlpatterns = [
    path('auth-drf/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
    path('posts/create/', PostCreateAPIView.as_view()),
    path('posts/update/<int:pk>/', PostUpdateAPIView.as_view()),
    path('posts/delete/<int:pk>/', PostDeleteAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/create/', CategoryCreateAPIView.as_view()),
    path('categories/delete/<int:pk>/', CategoryDeleteAPIView.as_view()),
    path('categories/update/<int:pk>/', CategoryUpdateAPIView.as_view()),
]
