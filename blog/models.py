from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    