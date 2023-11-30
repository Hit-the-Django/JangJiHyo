from rest_framework.serializers import ModelSerializer
from .models import Post, Comment

class PostModelSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        #fields=['id', 'writer', 'content']

class PostListModelSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        model=Post
        #fields='__all__'
        #fields=['id', 'writer', 'content']
        fields=[
            'id',
            'image',
            'created-at',
            'view_count',
            'writer',
        ]
        #exclude =['content',]
        depth = 1

class PostRetrieveSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        depth = 1

class PostCreateModelSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        model=Post
        fields=[
            'image',
            'content',
        ]

class PostDeleteModelSerializer(PostModelSerializer):
    pass

class CommentListModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'