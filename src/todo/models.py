from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

class TodoApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=300)
    description = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    is_complete = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    
    def __str__(self):
        return self.title