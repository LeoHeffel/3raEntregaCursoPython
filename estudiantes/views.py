from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models
from . import forms


# Create your views here.

def index(request):
    estudiantes= models.Estudiante.objects.all()
    contexto = {"estudiantes":estudiantes}
    return render(request, "estudiantes/index.html",contexto)

def crear(request):
    if request.method == "POST":
        form = forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiantes:index")
    else :
        form= forms.EstudianteForm
        return render(request, "estudiantes/crear.html", {"form":form})