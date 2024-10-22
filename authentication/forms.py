from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User



class UserRegistrationForm(forms.ModelForm):
    # Created 2 fields so we can compare them in clean method (by default django would give on password field)
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
    
    
    def clean(self):
        ''' Django always calles clean method behind the scenes whenever form is cleaned (submitted) '''
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password != password_confirm:
            raise forms.ValidationError('Password does not match!')
    
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['email'].label = ''

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].label = ''

        self.fields['password_confirm'].widget.attrs['class'] = 'form-control'
        self.fields['password_confirm'].widget.attrs['placeholder'] = 'Password Confirmation'
        self.fields['password_confirm'].label = ''
    
