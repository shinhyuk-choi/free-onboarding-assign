from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from post.models import Post
from post.serializers import PostSerializer


class PostViewSet(viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    ordering = '-id'

    def create(self, request):
        """
        POST /posts/

        data params
        - title(required)
        - content(required)
        """
        data = request.data
        if request.user.is_anonymous:
            raise NotAuthenticated
        if not data['title'] or not data['content']:
            return Response({"error": "title and content are required field."}, status=status.HTTP_400_BAD_REQUEST)
        post = Post.objects.create(title=data['title'], content=data['content'], author=request.user)
        return Response(self.get_serializer(post).data)

    def list(self, request):
        """
        GET /posts/

        query params
        - offset
        - limit
        """
        posts = Post.objects.all()
        paginator = self.paginator
        paginated_posts = paginator.paginate_queryset(posts, request)
        return paginator.get_paginated_response(self.get_serializer(paginated_posts, many=True).data)

    def retrieve(self, request, pk):
        """
        GET /posts/{post_id}/
        """
        post = get_object_or_404(Post, id=pk)
        return Response(self.get_serializer(post).data)

    def partial_update(self, request, pk):
        """
        PATCH /posts/{post_id}/
        """
        post = get_object_or_404(Post, id=pk)
        if post.author != request.user:
            raise PermissionDenied
        serializer = self.get_serializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(post, serializer.validated_data)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """
        DELETE /posts/{post_id}/
        """
        post = get_object_or_404(Post, id=pk)
        if post.author != request.user:
            raise PermissionDenied
        post.delete()
        return Response('{post deleted}')
