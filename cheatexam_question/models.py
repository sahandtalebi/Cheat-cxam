from django.db import models


class Question(models.Model):
    STATUS_CHOICES = [
        ('کم', 'poor'),
        ('زیاد', 'high'),
    ]

    message = models.TextField(verbose_name='سوال')
    answer = models.TextField(null=True,blank=True)
    #status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=False, verbose_name='اولویت')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

