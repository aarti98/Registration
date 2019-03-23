from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=200, blank=True)
    document    = models.FileField(upload_to='documents')
    uploaded_at = models.DateTimeField('Time',auto_now_add=True)

    def __str__(self):
        return self.description
