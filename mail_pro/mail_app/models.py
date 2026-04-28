from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfoModel(AbstractUser):
    full_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.full_name if self.full_name else self.username
    
    
class ContactModel(models.Model): 
    subject = models.CharField(max_length=255, null=True) 
    email = models.EmailField(null=True) 
    messages = models.TextField(null=True)

    def __str__(self):
        return f'{self.subject} - {self.email}'
