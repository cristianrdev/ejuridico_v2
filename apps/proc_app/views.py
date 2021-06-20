from django.shortcuts import render, redirect
from apps.users_app.models import Administrator, Court, Lawsuit_State, User, UserType
from apps.users_app.models import    Lawsuit, Defendant, LawsuitHistory
from django.db.models.query_utils import Q
from apps.proc_app.forms.new_movement import NewMovementForm2

# Create your views here.
def index(request):
    if not 'id' in request.session or request.session['user_type'] != "procuradora":
        return redirect('/')
    this_user= User.objects.get(id = int(request.session['id'])) 
    all_lawsuits = Lawsuit.objects.all()
    all_defendants = Defendant.objects.all()


    context = {
        'this_user' : this_user,
        'all_lawsuits' : all_lawsuits,
        'all_defendants' : all_defendants,
    }
    return render(request,'dashboard_procuradora.html', context)


def lawsuit_detail(request, id_lawsuit):
    if not 'id' in request.session or request.session['user_type'] != "procuradora":
        return redirect('/')
    this_user = User.objects.get(id = int(request.session['id'])) 
    this_lawsuit = Lawsuit.objects.get(id= id_lawsuit)
    this_defendant = this_lawsuit.current_defendant
    this_lawsuit_history = this_lawsuit.lawsuit_history
    # new_movement_form = NewMovementForm()
    current_state = this_lawsuit.current_demand_state
    new_movement_form = NewMovementForm2(initial= {'current_demand_state': current_state})

    estados = Lawsuit_State.objects.all()
    for i in estados:
        print(i.name_state)
        
    context = {
        'this_user' : this_user,
        'this_lawsuit' : this_lawsuit,
        'this_defendant' : this_defendant,
        'this_lawsuit_history' : this_lawsuit_history,
        'new_movement_form' : new_movement_form,
        

    }
    return render(request, "lawsuit_detail2.html", context)