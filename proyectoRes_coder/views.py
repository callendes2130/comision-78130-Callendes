from django.shortcuts import render, redirect, get_object_or_404
from coder.forms import *
from coder.models import T_Proceso
from django.contrib import messages

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

    
    







    



   



