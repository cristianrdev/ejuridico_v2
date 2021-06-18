from apps.users_app.models import Administrator, User, UserTyp
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
    this_user= User.objects.get(id = int(request.session['id'])) 
    if request.method == 'GET':
        defendantform = DefendantForm()
        context = {
        'defendantform' : defendantform,
            }
        return render(request, 'new_lawsuit.html',context)
    else: #si es post
        # lawsuitform = LawsuitForm(request.POST)
        defendantform = DefendantForm(request.POST)

        if defendantform.is_valid():
            print("ES valido"*10)
            # print(defendantform.first_name1)
            # si ambos son validos
            # new_lawsuit =lawsuitform.save(commit=False)
            # defendantform =defendantform.save(commit=False)
            # new_lawsuit.lawsuit_administrated_by = this_user
            new_defendant = defendantform.save(commit=False)
            new_defendant.defendant_created_by = this_user
            new_defendant.save()
            context = {
                'first_name1' : new_defendant.first_name1,
                'first_name2' : request.POST['first_name2'],
                'last_name1' : request.POST['last_name1'],
                'last_name2' : request.POST['last_name2'],

            }

            pdf = render_to_pdf('lawsuitpdf.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
            # return render(request, 'lawsuitpdf.html',context)

        # si no es válido
        print("no es valido"*10)
        context = {
            'defendantform' : defendantform,
        }
        return render(request, 'new_lawsuit.html',context)



# def make_lawsuit_document(request, lawsuitform):

#     pass
