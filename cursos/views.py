from django.shortcuts import redirect, render

from . import models
from . import forms


# Create your views here.

def index(request):
    cursos= models.Curso.objects.all()
    contexto = {"cursos":cursos}
    return render(request, "cursos/index.html",contexto)

def crear(request):
    if request.method == "POST":
        form = forms.CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cursos:index")
    else :
        form= forms.CursoForm
        return render(request, "cursos/crear.html", {"form":form})