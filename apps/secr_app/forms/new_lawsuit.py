from django.db.models.base import Model
from django import forms
from django.forms import ModelForm
from apps.users_app.models import Defendant
from apps.users_app.models import Lawsuit

class DefendantForm(ModelForm):
    class Meta:
        model = Defendant
        fields = ['first_name1','first_name2','last_name1','last_name2','address','rut']
        #widgets = {
            #'first_name1': forms.Textarea(attrs = {"class":"form-control ", "rows":4, "cols": "50%" , "style":"resize: none;"})}

        labels = {
                'first_name1': 'Primer Nombre',
                'first_name2': 'Segundo Nombre',
                'last_name1': 'Primer Apellido',
                'last_name2': 'Segundo Apellido',
                'address': 'Dirección Completa',
                'rut': 'RUT',
        }

class LawsuitForm(ModelForm):
    class Meta:
        model = Lawsuit
        fields = ['num_promissory_notes','final_date','mount_to_pay','num_operation','suscription_date','demand_amount']

        widgets = {
            'final_date': forms.Textarea(attrs = {"class":"form-control ", "rows":4, "cols": "50%" , "style":"resize: none;"})
            }

        labels ={
            'num_promissory_notes':'Número Pagaré',
            'final_date': 'Fecha MORA',
            'mount_to_pay': 'Monto a Pagar',
            'num_operation':'Número de Operación',
            'suscription_date':'Fecha Suscripción',
            'demand_amount':'Monto Demandado',
        }
