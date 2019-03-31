from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Document(models.Model):
    description = models.CharField(max_length=200, blank=True)
    document    = models.FileField(upload_to='documents')
    visible_to = models.ForeignKey(User,related_name='visible_to', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User,related_name='updated_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
