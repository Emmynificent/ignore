from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class NoteUserProfile(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name  = models.CharField(max_length= 25)
    email_address = models.EmailField(blank=True, unique=True)
    user_profile = models.OneToOneField(User, on_delete=models.SET_NULL, null = True)
    created = models.DateTimeField(auto_now_add=True, null = True)
    # age = models.DateField(auto_created=False)
    # id  =  models.UUIDField(default=uuid.uuid4, unique= True, primary_key =True, editable=True)
    
    
    def __str__(self):
        return self.first_name.capitalize()
    
 