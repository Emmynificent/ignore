from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User, AbstractUser
from .models import NoteUserProfile

class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']
        
    
class UserProfiling(ModelForm):
    class Meta:
        model = NoteUserProfile
        fields = ['first_name', 'last_name', 'email_address', ]
        
         