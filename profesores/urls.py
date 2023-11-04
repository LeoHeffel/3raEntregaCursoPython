
from django.urls import path
from . import views

app_name="profesores"

urlpatterns = [
    path("",views.ProfesoresList.as_view(),name="profesores_list"),
    path("detail/<int:pk>",views.ProfesoresDetail.as_view(),name="profesores_detail"),
    path("crear/",views.ProfesoresCreate.as_view(),name="profesores_create"),
    path("actualizar/<int:pk>",views.ProfesoresUpdate.as_view(),name="profesores_update"),
    path("borrar/<int:pk>",views.ProfesoresDelete.as_view(),name="profesores_delete"),
]
