from django.views.generic import TemplateView
from django.urls import path
from . import views

app_name="estudiantes"

urlpatterns = [
    path("",views.EstudiantesList.as_view(),name="estudiantes_list"),
    path("detail/<int:pk>",views.EstudiantesDetail.as_view(),name="estudiantes_detail"),
    path("crear/",views.EstudiantesCreate.as_view(),name="estudiantes_create"),
    path("actualizar/<int:pk>",views.EstudiantesUpdate.as_view(),name="estudiantes_update"),
    path("borrar/<int:pk>",views.EstudiantesDelete.as_view(),name="estudiantes_delete"),
]
