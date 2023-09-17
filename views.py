from django.shortcuts import render, redirect

from app.filters import EmployeFilter, MesureFilter
from app.forms import EmployeForm, MesureForm, ChargeForm
from app.models import Employe,Mesure, Charge


# Create your views here.


def accueil(request):
    coupures = Mesure.objects.filter(mesurer=True).order_by('-date_creation')[:6]
    ncoupures = Mesure.objects.filter(mesurer=False).order_by('-date_creation')[:6]
    context = {'coupures': coupures, 'ncoupures': ncoupures,}
    return render(request, 'app/accueil.html', context)


# ============================== MESURE =========================================
def add_mesure(request):
    if request.method == 'POST':
        form = MesureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_mesure')
    else:
        form = MesureForm()
    return render(request, 'app/add_mesure.html', {'form': form})


def update_mesure(request, pk):
    mesure = Mesure.objects.get(id=pk)
    form = MesureForm(instance=mesure)
    if request.method == 'POST':
        form = MesureForm(request.POST, instance=mesure)
        if form.is_valid():
            form.save()
            return redirect('list_mesure')
    context = {'form': form}
    return render(request, 'app/update_mesure.html', context)


def delete_mesure(request, pk):
    mesure = Mesure.objects.get(id=pk)
    if request.method == 'POST':
        mesure.delete()
        return redirect('list_mesure')
    context = {'mesure': mesure}
    return render(request, 'app/delete_mesure.html', context)


def list_mesure(request):
    mesures = Mesure.objects.all().order_by('-date_creation')
    total_mesure = mesures.count()
    myMesureFilter = MesureFilter(request.GET, queryset=mesures)
    mesures = myMesureFilter.qs
    context = {'mesures': mesures, 'total_mesure': total_mesure,'myMesureFilter': myMesureFilter,}
    return render(request, 'app/list_mesure.html', context)


def list_finance(request):
    finances = Mesure.objects.all().order_by('-date_creation')
    total_finance = finances.count()
    context = {'finances': finances, 'total_finance': total_finance,}
    return render(request, 'app/list_finance.html', context)

def detail_mesure(request,pk):
    mesure = Mesure.objects.get(id=pk)
    context = {'mesure':mesure}
    return render(request, 'app/detail_mesure.html', context)



# ==================       EMPLOYE  ====================================

def add_employe(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_employe')
    else:
        form = EmployeForm()
    return render(request, 'app/add_employe.html', {'form': form})


def list_employe(request):
    employes = Employe.objects.all().order_by('date_embauche')
    total_employe = employes.count()
    myEmployeFilter = EmployeFilter(request.GET, queryset=employes)
    employes = myEmployeFilter.qs
    context = {'employes': employes, 'total_employe': total_employe,'myEmployeFilter': myEmployeFilter, }
    return render(request, 'app/list_employe.html', context)



def detail_employe(request, pk):
    employe = Employe.objects.get(id=pk)
    context = {'employe': employe, }
    return render(request, 'app/detail_employe.html', context)


def update_employe(request, pk):
    employe = Employe.objects.get(id=pk)
    form = EmployeForm(instance=employe)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('list_employe')
    context = {'form': form}
    return render(request, 'app/update_employe.html', context)


def delete_employe(request, pk):
    employe = Employe.objects.get(id=pk)
    if request.method == 'POST':
        employe.delete()
        return redirect('list_employe')
    context = {'employe': employe}
    return render(request, 'app/delete_employe.html', context)



# ==================       CHARGES LIEES A L'EXPLOITATION  ====================================



def add_charge(request):
    if request.method == 'POST':
        form = ChargeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_charge')
    else:
        form = ChargeForm()
    return render(request, 'app/add_charge.html', {'form': form})


def list_charge(request):
    charges = Charge.objects.all()
    context = {'charges': charges, }
    return render(request, 'app/list_charge.html', context)


def detail_charge(request, pk):
    charge = Charge.objects.get(id=pk)
    context = {'charge': charge, }
    return render(request, 'app/detail_charge.html', context)


def update_charge(request, pk):
    charge = Charge.objects.get(id=pk)
    form = ChargeForm(instance=charge)
    if request.method == 'POST':
        form = ChargeForm(request.POST, instance=charge)
        if form.is_valid():
            form.save()
            return redirect('list_charge')
    context = {'form': form}
    return render(request, 'app/update_charge.html', context)


def delete_charge(request, pk):
    charge = Charge.objects.get(id=pk)
    if request.method == 'POST':
        charge.delete()
        return redirect('list_charge')
    context = {'charge': charge}
    return render(request, 'app/delete_charge.html', context)


# ====================================================
