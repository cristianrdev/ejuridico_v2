from django import forms
from django.forms import ModelForm
from apps.users_app.models import Lawsuit, LawsuitHistory, Lawsuit_State


class NewMovementForm2(ModelForm):
    class Meta:
        model = Lawsuit
        fields = ['current_demand_state']
        print(fields)

        widgets = {
            'current_demand_state': forms.Select( attrs = {"class":"form-control "},),
            }

        labels = {
                'current_demand_state': 'Cambiar de estado:',
        }