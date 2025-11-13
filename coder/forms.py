from django import forms
from coder.models import T_Proceso, T_Candidato,T_Entrevista

class T_ProcesoForm(forms.ModelForm):
    class Meta:
        model = T_Proceso
        fields = ["identificador","descripcion","cargo", "fechainicio","fechafin","totalpuestos"]
        wodgets = {
            #"identificador": forms.TextInput(attrs={'class': 'form-control'}),
            "identificador": forms.NumberInput(attrs={'class': 'form-control'}),
            "descripcion": forms.TextInput(attrs={'class': 'form-control'}),
            "cargo": forms.TextInput(attrs={'class': 'form-control'}),
            "fechainicio": forms.DateInput(attrs={'type':'date', 'class':'form-control'}) ,
            "fechafin": forms.DateInput(attrs={'type':'date', 'class':'form-control'}) ,            
            "totalpuestos": forms.NumberInput(attrs={'class':'form-control'})
        }

class T_CandidatoForm(forms.ModelForm):
    class Meta:
        model = T_Candidato
        fields = ["idPostulante","nombreC","apellidoC", "emailC","profesion"]
        wodgets = {
            "idPostulante": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreC": forms.TextInput(attrs={'class': 'form-control'}),
            "apellidoC": forms.TextInput(attrs={'class': 'form-control'}),
            "emailC": forms.EmailInput(attrs={'class': 'form-control'}),
            "profesion": forms.TextInput(attrs={'class': 'form-control'})
        }

class T_EntrevistaForm(forms.ModelForm):
    class Meta:
        model = T_Entrevista
        fields = ["idEntrevista","idProcesoE","idPostulanteE", "fechaE","nota"]
        widgets = {
            "idEntrevista": forms.NumberInput(attrs={'class':'form-control'}),
            "idProcesoE": forms.NumberInput(attrs={'class':'form-control'}),
            "idPostulanteE": forms.TextInput(attrs={'class': 'form-control'}),
            "fechaE": forms.DateInput(attrs={'type':'date', 'class':'form-control'}) ,
            "nota": forms.NumberInput(attrs={'class':'form-control'})
        }        
