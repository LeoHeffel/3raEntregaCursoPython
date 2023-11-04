from django.contrib.auth.mixins import LoginRequiredMixin
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

class ProfesoresCreate(LoginRequiredMixin,CreateView):
    login_url = 'home:login'
    model = models.Profesor
    form_class = forms.ProfesorForm
    success_url=reverse_lazy("profesores:profesores_list")

class ProfesoresUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'home:login'
    model = models.Profesor
    form_class = forms.ProfesorForm
    success_url=reverse_lazy("profesores:profesores_list")

class ProfesoresDelete(LoginRequiredMixin,DeleteView):
    login_url = 'home:login'
    model = models.Profesor
    success_url=reverse_lazy("profesores:profesores_list")