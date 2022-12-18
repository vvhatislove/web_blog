from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post, Category


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_pk')

    class Meta:
        model = User
        fields = ('id', 'username',)

    @staticmethod
    def get_pk(obj):
        return obj.pk


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('author',)


class PostReadSerializer(PostSerializer):
    category = CategorySerializer(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
