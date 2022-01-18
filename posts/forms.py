"""Posts form."""

# Djnago
from django import forms

# Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """POst model form."""
    class Meta:
        """Form Settings."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')