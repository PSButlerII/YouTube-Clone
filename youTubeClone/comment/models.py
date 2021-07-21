from django.db import models

class Comment(models.Model):
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    video_id = models.CharField(max_length=None)
    previous_comment = models.ForeignKey('comment.Comment', default=0, on_delete=models.PROTECT)
    comment = models.CharField(max_length=None)
