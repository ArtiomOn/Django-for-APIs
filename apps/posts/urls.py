from rest_framework_nested import routers
from apps.posts.views import PostViewSet, UserViewSet

base_router = routers.SimpleRouter()
base_router.register(r'users', UserViewSet, basename='users')
base_router.register(r'', PostViewSet, basename='posts')

urlpatterns = base_router.urls
