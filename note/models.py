from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from user.models import NoteUserProfile

class Note(models.Model):
    owner = models.ForeignKey(NoteUserProfile, on_delete=models.SET_NULL, blank = True, null=True)
    note_title = models.CharField(max_length=50, blank=True)
    note_content = models.TextField(blank=True)
    note_created = models.DateTimeField(auto_now_add = True)
    note_updated = models.DateTimeField(auto_now=True)
    note_owner = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    
    def __str__(self):
        return self.note_title.capitalize()
    
    
    