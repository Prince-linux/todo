from django.db import models

class TodoItem(models.Model):
    content = models.TextField()
    author = models.TextField()
    date_created = models.DateTimeField()
    completed = models.BooleanField()
