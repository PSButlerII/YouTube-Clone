from django.db import models


# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    videoId = models.ForeignKey()
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    comment_reply = models.TextField()
