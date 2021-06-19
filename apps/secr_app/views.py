import re
from django.db.models.query_utils import Q
from apps.users_app.models import Administrator, Court, Lawsuit_State, User, UserType
from django.shortcuts import redirect, render
from apps.users_app.forms.register import UserForm
from .forms.new_lawsuit import LawsuitForm, DefendantForm
from apps.users_app.models import    Lawsuit, Defendant
from .utils import render_to_pdf
from django.http import HttpResponse
# 

def index(request):
    if not 'id' in request.session or request.session['user_type'] != "secretaria":
        return redirect('/')
    this_user= User.objects.get(id = int(request.session['id'])) 
    all_lawsuits = Lawsuit.objects.all()
    all_defendants = Defendant.objects.all()


    context = {
        'this_user' : this_user,
        'all_lawsuits' : all_lawsuits,
        'all_defendants' : all_defendants,
    }
    return render(request, 'dashboard_secretary.html', context)


def create_lawsuit(request):
    if not 'id' in request.session or request.session['user_type'] != "secretaria":
        return redirect('/')
    this_user= User.objects.get(id = int(request.session['id'])) 
    if request.method == 'GET':
        defendantform = DefendantForm()
        lawsuitform = LawsuitForm()
        context = {
        'defendantform' : defendantform,
        'lawsuitform' : lawsuitform,
            }
        return render(request, 'new_lawsuit.html',context)
    else: #si es post
        lawsuitform = LawsuitForm(request.POST)
        defendantform = DefendantForm(request.POST)

        if defendantform.is_valid() and lawsuitform.is_valid():
            print("ES valido"*10)

            new_defendant = defendantform.save(commit=False) #guarda al demandado
            new_defendant.defendant_created_by = this_user 
            new_defendant.save()

            new_lawsuit = lawsuitform.save(commit=False)
            new_lawsuit.current_court = Court.objects.get(cod_tribunal = "00")
            new_lawsuit.current_demand_state = Lawsuit_State.objects.get(name_state = "escritura creada")
            new_lawsuit.current_defendant = new_defendant
            new_lawsuit.lawsuit_created_by = this_user
            new_lawsuit.save()



            context = {
                # 'first_name1' : new_defendant.first_name1,
                # 'first_name2' : new_defendant.first_name2,
                # 'last_name1' : new_defendant.last_name1,
                # 'last_name2' : new_defendant.last_name2,
                # 'address' : new_defendant.address,
                # 'rut' : new_defendant.rut,

                # 'new_lawsuit' : new_lawsuit.num_promissory_notes,
                # 'rut' : new_lawsuit.final_date,
                # 'rut' : new_lawsuit.rut,
                'defendant' : new_defendant,
                'lawsuit' : new_lawsuit,

            }

            pdf = render_to_pdf('lawsuitpdf.html', context)
            
            return  HttpResponse(pdf, content_type='application/pdf')
            # return render(request, 'lawsuitpdf.html',context)

        # si no es válido
        print("no es valido"*10)
        context = {
            'defendantform' : defendantform,
        }
        return render(request, 'new_lawsuit.html',context)

def delete_lawsuit(request, id_lawsuit):
    if not 'id' in request.session or request.session['user_type'] != "secretaria":
        return redirect('/')
    this_lawsuit = Lawsuit.objects.get(id = id_lawsuit )
    print(f"se borrarla la demanda id = {this_lawsuit.id}")
    this_lawsuit.delete()
    return redirect('/')


# def make_lawsuit_document(request, lawsuitform):

#     pass
