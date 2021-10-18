from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'content',
        )

    def validate(self, data):
        if 'author' in data.keys():
            raise serializers.ValidationError({'author': 'Could not be modified'})
        return super(PostSerializer, self).validate(data)
