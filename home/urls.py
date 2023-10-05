from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name="home"

urlpatterns = [
    path("",views.index, name="index"),
    path("about/",views.about, name="about"),
    path("login/",views.login_request, name="login"),
    path("register/",views.register, name="register"),
    path("logout/",LogoutView.as_view(template_name="home/index.html"), name="logout")
]
urlpatterns += staticfiles_urlpatterns()