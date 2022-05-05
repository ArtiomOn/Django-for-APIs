from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

from apps.posts.models import Post

User = get_user_model()


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at', 'updated_at')


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')
