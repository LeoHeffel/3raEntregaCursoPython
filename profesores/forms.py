from django import forms
from . import models

class ProfesorForm(forms.ModelForm):
    class Meta:
        model= models.Profesor
        fields=["nombre","apellido","email"]