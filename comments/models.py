from django.db import models
from django.utils import timezone


class Post(models.Model):
    content = models.CharField(max_length=30000)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:50]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
