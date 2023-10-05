from django import forms
from django.contrib.auth.forms import UserModel, UserCreationForm,AuthenticationForm


class UserCreationFormCustom(UserCreationForm):
    username= forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    password1= forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    password2= forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    class Meta:
        model= UserModel
        fields=["username","password1","password2"]
        help_text= {
            k:"" for k in fields
        }
    
class AuthenticationFormCustom(AuthenticationForm):
    username= forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    password= forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    class Meta:
        model= UserModel
        fields=["username","password1","password2"]
        help_text= {
            k:"" for k in fields
        }