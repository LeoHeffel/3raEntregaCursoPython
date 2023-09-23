from django.db import models

# Create your models here.
class Curso(models.Model):
    curso=models.CharField(max_length=100)
    camada=models.CharField(max_length=100)
    
    

    def __str__(self) -> str:
        return f"{self.curso} {self.camada}"