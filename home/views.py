from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


from home.forms import UserCreationFormCustom,AuthenticationFormCustom
# Create your views here.

def index(request):
    
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationFormCustom(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasena)
            login(request, user)
            return render(request, "home/index.html")
    else:
        form = AuthenticationFormCustom()
    return render(request, "home/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            form.save()
            return render(request, "home/index.html")
    else:
        form = UserCreationFormCustom()
    return render(request, "home/register.html", {"form": form})