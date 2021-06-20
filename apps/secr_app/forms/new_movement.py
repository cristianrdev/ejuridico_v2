from django import forms
from django.db.models import query
from django.forms import ModelForm
from apps.users_app.models import Lawsuit, LawsuitHistory, Lawsuit_State


class NewMovementForm(ModelForm):
    class Meta:
        model = Lawsuit
        fields = ['current_demand_state']

        widgets = {
            
            'current_demand_state': forms.Select( attrs = {"class":"form-control "}),


            }

        labels = {
                'current_demand_state': 'Cambiar de estado:',

        }
    # def __init__(self, name_state, *args, **kwargs):
    #     super(NewMovementForm, self).__init__(*args, **kwargs)
    #     self.fields['name_state'].queryset = Lawsuit.objects.filter(current_demand_state__name_state__in = ["caratula asignada", "escritura creada"])


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Seleccione el documento')
