from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'like')
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['title'].label = ''

        
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['description'].label = ''

        
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['placeholder'] = 'Image'
        self.fields['image'].label = ''


