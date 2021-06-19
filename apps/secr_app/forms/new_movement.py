from django import forms
from django.forms import ModelForm
from apps.users_app.models import Lawsuit, LawsuitHistory, Lawsuit_State


class NewMovementForm(ModelForm):
    class Meta:
        model = Lawsuit
        fields = ['current_demand_state']

        widgets = {
            
            'current_demand_state': forms.Select( attrs = {"class":"form-control "},),


            }

        labels = {
                'current_demand_state': 'Cambiar de estado:',

        }


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Seleccione el documento')
