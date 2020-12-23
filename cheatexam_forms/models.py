from django.contrib.auth.models import User
from django.db import models

User = User()

class Forms(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, primary_key=True)
    password = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name