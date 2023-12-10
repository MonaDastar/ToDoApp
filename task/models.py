from django.db import models
from datetime import timedelta
from django.utils import timezone


def in_three_days():
    return timezone.now() + timedelta(days=3)


class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    address = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt= models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    due_date= models.DateField(default=in_three_days)
    done = models.BooleanField(default=False)
    #users = models.ManyToManyField(User)  # Many-to-Many relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user}-{self.title}"
    
    class Meta:
        # Add the unique_together constraint
        unique_together = ['user', 'title']