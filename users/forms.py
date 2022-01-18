"""User forms"""

# Django
import profile
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile

class SignUpForm(forms.Form):
    """Sign Up form"""

    username = forms.CharField(label=False,min_length=4,max_length=50, widget = forms.TextInput(attrs={'placeholder':'Nombre de usuario','class': 'form-control','required': True}))

    password = forms.CharField(label=False,max_length=70, widget=forms.PasswordInput(attrs={'placeholder':'Escribe tu contraseña','class': 'form-control','required': True}))

    password_confirmation = forms.CharField(label=False,max_length=70, widget=forms.PasswordInput(attrs={'placeholder':'Confirma tu contraseña','class': 'form-control','required': True}))

    first_name = forms.CharField(label=False,min_length=2,max_length=50,widget = forms.TextInput(attrs={'placeholder':'Nombres','class': 'form-control','required': True}))

    last_name = forms.CharField(label=False,min_length=2,max_length=50,widget = forms.TextInput(attrs={'placeholder':'Apellidos','class': 'form-control','required': True}))

    email = forms.EmailField(label=False,min_length=6,max_length=70,widget=forms.EmailInput(attrs={'placeholder':'Correo electrónico','class': 'form-control','required': True}))

    # validate only one atrbute
    def clean_username(self):
        """Username must be unique."""
        
        username = self.cleaned_data['username']
        # Query a la base de datos
        q = User.objects.filter(username=username).exists()
        if q:
            raise forms.ValidationError('Username is already in use.')
        else:
            # siempre que hagas la validación de un dato debes devolver el dato
            return username
    
    # validar la contraseña
    def clean(self):
        """Verify password and pw confirmation match"""
        # traer la data para no sobreescribir el clean
        data = super().clean()
        
        password = data['password']
        password_confirmation = data['password_confirmation']
        
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')

        return data
    
    # salvar el form
    
    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()