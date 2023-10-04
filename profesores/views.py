from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from . import models
from . import forms


# Create your views here.

class ProfesoresList(ListView):
    model = models.Profesor

    def get_queryset(self):
        object_list = models.Profesor.objects.all()
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.Profesor.objects.filter(
                nombre__icontains=consulta
            )
        return object_list

class ProfesoresDetail(DetailView):
    model = models.Profesor

class ProfesoresCreate(CreateView):
    model = models.Profesor
    form_class = forms.ProfesorForm
    success_url=reverse_lazy("profesores:profesores_list")

class ProfesoresUpdate(UpdateView):
    model = models.Profesor
    form_class = forms.ProfesorForm
    success_url=reverse_lazy("profesores:profesores_list")

class ProfesoresDelete(DeleteView):
    model = models.Profesor
    success_url=reverse_lazy("profesores:profesores_list")