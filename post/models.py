from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PostModel(models.Model):
    # user = models.ForeignKey(User, related_name='post',on_delete=models.CASCADE)
    caption = models.CharField(max_length=3000)
    created_on = models.DateTimeField(auto_now_add=True)
    # like_dislike = models.OneToOneField(LikeDislikeModel,on_delete = models.CASCADE,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    post_image = models.ImageField(upload_to='post/media/images/',null=True,blank=True)
    
    
    def __str__(self):
        return f'post {self.caption}'
    

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    # user = 
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # j somoy ei class er object creae hobe thikon current time ta rekhe dibe
    
    def __str__(self):
        return f'coomment by {self.post.caption}'