from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth.models import User

User = get_user_model()


class Question(models.Model):
    message = models.TextField(verbose_name='سوال')
    answer = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=False, null=True)

    def str(self):
        return self.message

