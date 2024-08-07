from .models import Post
from django import forms

class PostCreatForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','image','caption')