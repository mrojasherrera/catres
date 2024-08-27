from django import forms

class ResolucionesSearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=255, required=False,                      widget=forms.TextInput(attrs={'placeholder': 'Buscar por número, sumario o observaciones...'}))
