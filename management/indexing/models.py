from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    context_embedding = models.JSONField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.title