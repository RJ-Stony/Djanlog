from django.db import models
import os

class Post(models.Model):
    title = models.CharField(max_length=50)
    hook = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.upload.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    