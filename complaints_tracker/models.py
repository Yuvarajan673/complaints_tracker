from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<username>/<filename>
    return os.path.join(instance.user.username, filename)


class Complaint(models.Model):
    CATEGORY_CHOICES=[
        ('road','Road Damage'),
        ('water','Water Problem'),
        ('light','Street Light Issue'),
        ('garbage','Garbage Issue'),
        ('others','Other Issues'),
    ]

    STATUS_CHOICES=[
        ('pending','Pending'),
        ('in_progress','In Progress'),
        ('resolved','Resolved'),
    ]

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES,default='pending')
    image=models.ImageField(upload_to=user_directory_path)
    location=models.CharField(max_length=255)
    creation_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    