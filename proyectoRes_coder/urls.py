"""
URL configuration for proyectoRes_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, test, crear_proceso, crear_candidato, crear_entrevista, lista_procesos, eliminar_proceso, modificar_proceso, acerca, lista_candidato, modificar_candidato, eliminar_candidato, update_proceso, lista_entrevista, modificar_entrevista, eliminar_entrevista, visualizar_proceso, visualizar_candidato, visualizar_entrevista
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("test/", test, name="test"), 

    path("proceso/nuevo", crear_proceso, name  = "proceso_form"),     
    path("procesos/", lista_procesos, name="proceso_list"),
    path("proceso/<int:identificador>/eliminar", eliminar_proceso, name="eliminar_proceso"),
    path("proceso/<int:identificador>/modificar", modificar_proceso, name="modificar_proceso"),
    path("proceso/<int:identificador>/ver", visualizar_proceso, name="visualizar_proceso"),

    path("entrevista/nuevo", crear_entrevista, name  = "entrevista_form"),
    path("entrevistas/", lista_entrevista, name="entrevista_list"),
    path("entrevista/<int:idEntrevista>/eliminar", eliminar_entrevista, name="eliminar_entrevista"), 
    path("entrevista/<int:idEntrevista>/modificar", modificar_entrevista, name="modificar_entrevista"),
    path("entrevista/<int:idEntrevista>/ver", visualizar_entrevista, name="visualizar_entrevista"),
    
    path("candidato/nuevo", crear_candidato, name  = "candidato_form"),  
    path("candidatos/", lista_candidato, name="candidato_list"),    
    path("candidatos/<str:idPostulante>/eliminar", eliminar_candidato, name="eliminar_candidato"),                
    path("candidatos/<str:idPostulante>/modificar", modificar_candidato, name="modificar_candidato"),
    path("candidatos/<str:idPostulante>/ver", visualizar_candidato, name="visualizar_candidato"),
    
    path("cursos/", include("cursos.urls")),
    path("", include("accounts.urls")),
    path("acerca/", acerca, name = "acerca"),       
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


