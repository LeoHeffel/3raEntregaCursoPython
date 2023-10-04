from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models
from . import forms


# Create your views here.

class EstudiantesList(ListView):
    model = models.Estudiante

    def get_queryset(self):
        object_list = models.Estudiante.objects.all()
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.Estudiante.objects.filter(
                nombre__icontains=consulta
            )
        return object_list

class EstudiantesDetail(DetailView):
    model = models.Estudiante

class EstudiantesCreate(CreateView):
    model = models.Estudiante
    form_class = forms.EstudianteForm
    success_url=reverse_lazy("estudiantes:estudiantes_list")

class EstudiantesUpdate(UpdateView):
    model = models.Estudiante
    form_class = forms.EstudianteForm
    success_url=reverse_lazy("estudiantes:estudiantes_list")

class EstudiantesDelete(DeleteView):
    model = models.Estudiante
    success_url=reverse_lazy("estudiantes:estudiantes_list")