from django import forms
from django.forms import ValidationError

from .models import Profile
from authentication.models import User

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']



class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
        
    def clean_username(self):
        username = self.cleaned_data['username']
        
        # Check if the form has an instance (the user being edited)
        if self.instance:  # The instance attribute is set when pass an instance of the model to the form- UserForm(instance=user).
            # If the username is the same as the current user's username allw it
            if username == self.instance.username:
                return username
        
        # Otherwise, check if any other user has the same username
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        
        return username
