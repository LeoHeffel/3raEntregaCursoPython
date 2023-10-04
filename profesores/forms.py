from django import forms
from . import models

class ProfesorForm(forms.ModelForm):
    class Meta:
        model= models.Profesor
        fields=["nombre","apellido","email"]

        widgets= {
            "nombre":forms.TextInput(attrs={"class":"form-control"}),
            "apellido":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"})
        }
    