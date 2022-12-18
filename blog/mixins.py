from blog.models import Post, Category
from blog.serializers import PostSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostMixin:
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryMixin:
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
