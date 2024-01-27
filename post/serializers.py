from rest_framework import serializers
from .import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostModel
        fields = ['caption','body','post_image']
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentModel
        fields = ['post','body']