from django.db import models
from django.contrib.auth.models import User
from notices.models import Notice


class Comment(models.Model):
    """ Model for comments """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)