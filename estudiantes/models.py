from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    nacimiento=models.DateField(null=True)
    # curso=models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"