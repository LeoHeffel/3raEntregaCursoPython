
from django.urls import path
from . import views

app_name="cursos"

urlpatterns = [
    path("",views.CursosList.as_view(),name="cursos_list"),
    path("detail/<int:pk>",views.CursosDetail.as_view(),name="cursos_detail"),
    path("crear/",views.CursosCreate.as_view(),name="cursos_create"),
    path("actualizar/<int:pk>",views.CursosUpdate.as_view(),name="cursos_update"),
    path("borrar/<int:pk>",views.CursosDelete.as_view(),name="cursos_delete"),
]
