from django.urls import path, include
from rest_framework.routers import SimpleRouter

from post.views import PostViewSet

app_name = 'post'

router = SimpleRouter()

router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include((router.urls, 'post')))
]
