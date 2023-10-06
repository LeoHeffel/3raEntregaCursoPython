from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from . import models
from . import forms


# Create your views here.

class CursosList(ListView):
    model = models.Curso

    def get_queryset(self):
        object_list = models.Curso.objects.all()
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.Curso.objects.filter(
                curso__icontains=consulta
            )
        return object_list

class CursosDetail(DetailView):
    model = models.Curso

class CursosCreate(LoginRequiredMixin,CreateView):
    login_url = 'home:login'
    model = models.Curso
    form_class = forms.CursoForm
    success_url=reverse_lazy("cursos:cursos_list")

class CursosUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'home:login'
    model = models.Curso
    form_class = forms.CursoForm
    success_url=reverse_lazy("cursos:cursos_list")

class CursosDelete(LoginRequiredMixin,DeleteView):
    login_url = 'home:login'
    model = models.Curso
    success_url=reverse_lazy("cursos:cursos_list")