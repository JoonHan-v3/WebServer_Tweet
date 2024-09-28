from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
# Create your models here.
class Twit(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='twits')
    body=models.TextField()
    image=models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True)
    created_date=models.DateTimeField(default=timezone.now)
    users_like=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='twits_liked')
    
    class Meta:
        ordering=('-created_date',)

    #def get_absolute_url(self)

class Comment(models.Model):
    twit=models.ForeignKey(Twit, on_delete=models.CASCADE, related_name='twit_comments')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    body=models.TextField()
    created_datetime=models.DateTimeField(auto_now_add=True)
    updated_datetime=models.DateTimeField(auto_now=True)
    class Mets:
        ordering=('-created_datetime')
    def __str__(self):
        return self.body
        
