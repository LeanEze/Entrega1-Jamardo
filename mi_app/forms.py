from django import forms



class perroFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    raza = forms.CharField(max_length=40)
    edad = forms.IntegerField()

class gatoFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    raza = forms.CharField(max_length=40)
    edad = forms.IntegerField()

class cerdoFormulario(forms.Form):
   
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    raza = forms.CharField(max_length=40)
    edad = forms.IntegerField()