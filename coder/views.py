from django.shortcuts import render
#from coder.app forms import *
# Create your views here.

def index(request):   
    return render(request,"coder/index.html")
    #return render(request,"C:/ProyectoPython/comision-78130-Callendes/coder/templates/coder/index.html")
   



