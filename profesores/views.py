from django.shortcuts import redirect, render

from . import models
from . import forms

# Create your views here.

def index(request):
    profesores= models.Profesor.objects.all()
    contexto = {"profesores":profesores}
    return render(request, "profesores/index.html",contexto)

def crear(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesores:index")
    else :
        form= forms.ProfesorForm
        return render(request, "profesores/crear.html", {"form":form})