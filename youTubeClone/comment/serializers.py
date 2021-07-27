from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'likes', 'dislikes', 'video_id', 'new_comment', 'previous_comment']
