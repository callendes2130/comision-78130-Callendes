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
from .views import index, test, crear_proceso, crear_candidato, crear_entrevista, lista_procesos, eliminar_proceso, modificar_proceso, acerca


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("test/", test, name="test"), 
    path("proceso/nuevo", crear_proceso, name  = "proceso_form"), 
    path("candidato/nuevo", crear_candidato, name  = "candidato_form"),
    path("entrevista/nuevo", crear_entrevista, name  = "entrevista_form"),
    path("procesos/", lista_procesos, name="proceso_list"),
    path("proceso/<int:identificador>/eliminar", eliminar_proceso, name="eliminar_proceso"),
    path("proceso/<int:identificador>/modificar", modificar_proceso, name="modificar_proceso"),
    path("cursos/", include("cursos.urls")),
    path("", include("accounts.urls")),
    path("acerca/", acerca, name = "acerca"),       
]

#C:\ProyectoPython\comision-78130-Callendes\accounts\urls.py
#C:\ProyectoPython\comision-78130-Callendes\coder\templates\coder\index.html
#C:\ProyectoPython\comision-78130-Callendes\entorno_virtual\Lib\site-packages\django\contrib\admin\templates\coder\index.html 


#from django.contrib import admin
#from django.urls import path, include
#from . import views
##from .views import index, test

#urlpatterns = [
#    path("admin/", admin.site.urls),
#    path('', views.index),
#    path("coder/", include("coder.urls")),
#    path("test/", views.test),

