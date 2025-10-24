from django.shortcuts import render, redirect
from coder.forms import *
from coder.models import T_Proceso

def index(request):   
    return render(request,"index.html")

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



    



   



