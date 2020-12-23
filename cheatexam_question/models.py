from django.contrib.auth import get_user_model
from cheatexam_forms.models import Forms
from django.db import models
from django.contrib.auth.models import User

User = get_user_model()


class Question(models.Model):
    message = models.TextField(verbose_name='سوال', primary_key=True)
    answer = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=False, null=True)
    #form = models.ForeignKey(Forms, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

