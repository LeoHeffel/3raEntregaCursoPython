from django import forms
from . import models

class CursoForm(forms.ModelForm):
    class Meta:
        model= models.Curso
        fields=["curso","camada"]
    
        widgets= {
                "curso":forms.TextInput(attrs={"class":"form-control"}),
                "camada":forms.TextInput(attrs={"class":"form-control"})
            }