from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title) + ' ' + self.content
