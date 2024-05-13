# models.py

from django.db import models
from django.contrib.auth.models import User  # Assuming you're using Django's built-in User model for authentication

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
