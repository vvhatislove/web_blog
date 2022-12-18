from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from blog.mixins import PostMixin, CategoryMixin
from blog.serializers import PostReadSerializer


# Create your views here.


class PostListAPIView(PostMixin, generics.ListAPIView):
    serializer_class = PostReadSerializer


class PostCreateAPIView(PostMixin, generics.CreateAPIView):
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdateAPIView(PostMixin, generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)


class PostDeleteAPIView(PostMixin, generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)


class PostDetailAPIView(PostMixin, generics.RetrieveAPIView):
    serializer_class = PostReadSerializer


class CategoryDetailAPIView(CategoryMixin, generics.RetrieveAPIView):
    pass


class CategoryCreateAPIView(CategoryMixin, generics.CreateAPIView):
    permission_classes = (IsAdminUser,)


class CategoryDeleteAPIView(CategoryMixin, generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)


class CategoryUpdateAPIView(CategoryMixin, generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)


class CategoryListAPIView(CategoryMixin, generics.ListAPIView):
    pass
