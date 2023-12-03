from django.db import models


class FacebookPost(models.Model):
    post_id = models.CharField(max_length=255, null=True, blank=True)
    post_link = models.CharField(max_length=255)
    publish_time = models.DateTimeField()
    content = models.TextField()
    likes = models.IntegerField(null=True)
    reaction_count = models.IntegerField()
    reaction_type = models.JSONField(null=True)
    comment_count = models.IntegerField(null=True)

    def __str__(self):
        return f"Content: {self.content}"
