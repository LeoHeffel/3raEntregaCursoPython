from django import forms
from . import models

class EstudianteForm(forms.ModelForm):
    class Meta:
        model= models.Estudiante
        fields=["nombre","apellido","nacimiento"]

        widgets= {
            "nombre":forms.TextInput(attrs={"class":"form-control"}),
            "apellido":forms.TextInput(attrs={"class":"form-control"}),
            "nacimiento":forms.DateInput(attrs={"class":"form-control"})
        }