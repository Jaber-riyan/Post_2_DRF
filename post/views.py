from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .serializers import PostSerializer, CommentSerializer

# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    queryset = models.PostModel.objects.all()
    serializer_class = PostSerializer
    
    
    
class CommentViewset(viewsets.ModelViewSet):
    queryset = models.CommentModel.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.request.query_params)
        post_id = self.request.query_params.get('id')
        print(post_id)
        if post_id:
            queryset = queryset.filter(post__id=post_id)
        return queryset
