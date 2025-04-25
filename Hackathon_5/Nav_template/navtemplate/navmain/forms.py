from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):

    class Meta:

        model = Incident
        fields = ['name', 'location', 'incident_type', 'description','age']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'location': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'incident_type': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'rows': 4}),
            'age': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
        }
 