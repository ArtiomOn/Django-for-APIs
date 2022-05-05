from django.contrib.auth import get_user_model

from rest_framework.viewsets import GenericViewSet, ModelViewSet

from apps.posts.serializers import PostSerializer, UserSerializer
from apps.posts.models import Post
from apps.posts.permissions import IsAuthorOrReadOnly

User = get_user_model()


class PostViewSet(
    ModelViewSet,
    GenericViewSet
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class UserViewSet(
    ModelViewSet,
    GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
