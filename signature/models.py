from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Signature(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='signatures')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signed_at = models.DateTimeField(auto_now_add=True)
    signature_image = models.ImageField(upload_to='signatures/')

    def __str__(self):
        return f"{self.user.username} - {self.document.title}"