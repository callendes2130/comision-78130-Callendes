from django.shortcuts import render
#from coder.app forms import *
# Create your views here.

def index(request):   
    return render(request,"index.html")

def test(request):
    return render(request, "test.html")

#C:\ProyectoPython\comision-78130-Callendes\proyectoRes_coder\templates\coder\test.html




