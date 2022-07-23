from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

class TodoApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    todo = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=datetime.now)
    is_complete = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.user.username