from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from coder.forms import *
from coder.models import T_Proceso, T_Candidato, T_Entrevista
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from coder.forms import T_ProcesoForm
from coder.models import T_Proceso


from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):   
    return render(request,"index.html")

def acerca(request):   
    return render(request,"acerca.html")

def test(request):
    return render(request, "test.html")

def crear_proceso(request):
    # GET - Pedir informacion a la base de datos
    # POST - Solicitud para crear/manipular información
    if request.method == "POST":
        form = T_ProcesoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proceso_form")
    else:
        form = T_ProcesoForm()
    return render(request, "proceso_form.html", {'form':form})

def lista_procesos(request):
    query = request.GET.get('q','' )
    if len(query) > 0: #if query
        proceso =  T_Proceso.objects.filter (
            identificador__icontains=query).order_by("-fechainicio")
    else:
        proceso = T_Proceso.objects.all(). order_by("-fechainicio")
    return render(request, "proceso_list.html", {"proceso": proceso, "query":query})

def eliminar_proceso(request, identificador):
    #si este metodo me devuelve 2 o más registros arroja error MultipleObject
    #sino existe registro con ese id error DoesNotExist   
    #proceso = T_Proceso.objects.get(identi = idpro)   
    proceso = get_object_or_404(T_Proceso, identificador = identificador)
    proceso.delete()
    messages.success(request, "Proceso eliminado correctamente")
    return redirect("proceso_list")

def modificar_proceso(request, identificador):
    proceso = get_object_or_404(T_Proceso, identificador = identificador)
    if request.method == "POST":
        form = T_ProcesoForm(request.POST, instance=proceso)
        if form.is_valid():
            form.save()
            return redirect("proceso_form")
    else:
        form = T_ProcesoForm(instance=proceso)
    return render(request, "proceso_form.html", {'form':form, 'edicion':True})

def visualizar_proceso(request, identificador):
    proceso = get_object_or_404(T_Proceso, identificador=identificador)
    return render(request, "proceso_ver.html", {'proceso': proceso})

class update_proceso(LoginRequiredMixin, UpdateView):
    model = T_Proceso
    form_class = T_ProcesoForm
    template_name = 'proceso_form.html'
    success_url = reverse_lazy('proceso_list')
    # usar RUT como slug:
    slug_field = 'identificador'
    slug_url_kwarg = 'identificador'


#-----------------------------------------------------------------------------

def crear_candidato(request):
    # GET - Pedir informacion a la base de datos
    # POST - Solicitud para crear/manipular información
    if request.method == "POST":
        form = T_CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("candidato_form")
    else:
        form = T_CandidatoForm()
    return render(request, "candidato_form.html", {'form':form})


def lista_candidato(request):
    query2 = request.GET.get('q','' )
    if len(query2) > 0: #if query
        candidato =  T_Candidato.objects.filter (idPostulante__icontains=query2).order_by("-nombreC")
    else:
        candidato = T_Candidato.objects.all(). order_by("-nombreC")
    return render(request, "candidato_list.html", {"candidato": candidato, "query":query2})

def eliminar_candidato(request, idPostulante):
    candidato = get_object_or_404(T_Candidato, idPostulante = idPostulante)
    candidato.delete()
    messages.success(request, "Candidato eliminado correctamente")
    return redirect("candidato_list")

def modificar_candidato(request, idPostulante):
    candidato = get_object_or_404(T_Candidato, idPostulante = idPostulante)
    if request.method == "POST":
        form = T_CandidatoForm(request.POST, instance=candidato)
        if form.is_valid():
            form.save()
            return redirect("candidato_form")
    else:
        form = T_CandidatoForm (instance=candidato)
    return render(request, "candidato_form.html", {'form':form, 'edicion':True})

def visualizar_candidato(request, idPostulante):
    candidato = get_object_or_404(T_Candidato, idPostulante = idPostulante)
    return render(request, "candidato_ver.html", {'candidato': candidato})

#-------------------------------------------------------------------------------
def crear_entrevista(request):
    # GET - Pedir informacion a la base de datos
    # POST - Solicitud para crear/manipular información
    if request.method == "POST":
        form = T_EntrevistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("entrevista_form")
    else:
        form = T_EntrevistaForm()
    return render(request, "entrevista_form.html", {'form':form})


def lista_entrevista(request):
    query3 = request.GET.get('q','' )
    if len(query3) > 0: #if query
        entrevista =  T_Entrevista.objects.filter (idEntrevista__icontains=query3).order_by("-idPostulanteE")
    else:
        entrevista =  T_Entrevista.objects.all(). order_by("-idPostulanteE")
    return render(request, "entrevista_list.html", {"entrevista": entrevista, "query":query3})

def modificar_entrevista(request, idEntrevista):
    entrevista = get_object_or_404(T_Entrevista, idEntrevista = idEntrevista)
    if request.method == "POST":
        form = T_EntrevistaForm(request.POST, instance=entrevista)
        if form.is_valid():
            form.save()
            return redirect("entrevista_form")
    else:
        form = T_EntrevistaForm (instance=entrevista)
    return render(request, "entrevista_form.html", {'form':form, 'edicion':True})

def eliminar_entrevista(request, idEntrevista):
    entrevista = get_object_or_404(T_Entrevista , idEntrevista = idEntrevista)
    entrevista.delete()
    messages.success(request, "Entrevista eliminada correctamente")
    return redirect("entrevista_list")

def visualizar_entrevista(request, idEntrevista):
    entrevista = get_object_or_404(T_Entrevista, idEntrevista = idEntrevista)
    return render(request, "entrevista_ver.html", {'entrevista': entrevista})
    







    



   



