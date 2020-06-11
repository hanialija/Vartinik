from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,  JsonResponse
from .models import Card, CardForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def katalog(request):
    lista = Card.objects.order_by('-data')
    param = {
        'listaC': lista
    }
    return render(request, 'katalog/templates/katalog.html', param)

def regjistro(request):
        # pasi mbushet formulari
        if request.method == "POST":
            form = CardForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(commit=False)
                form.foto = request.FILES['foto']
                form.save()
                return redirect('/katalog/')
        else:# shfaqja e formularit per nje vleresim te ri
            form = CardForm()
        
        parametrat = {
            'forma': form,
            'mode': "Shto"
        }
        return render(request, 'katalog/templates/form.html', parametrat)
@csrf_exempt
def fshi(request, id):
    fs = get_object_or_404(Card, pk=id)
    # pasi behet submit fshirja
    if request.method == "POST":
        fs.delete()
        return JsonResponse(True, safe = False) 
    else:
        return JsonResponse(False, safe = False)

def edit(request, id):
    newCard = get_object_or_404(Card, id=id)
    # thirret pasi behet submit ndryshimi
    if request.method == "POST":
        form = CardForm(request.POST, instance=newCard)
        if form.is_valid():
            form.save()
            return redirect('../../')
    else:
        form = CardForm(instance=newCard)
    # kur hapet formulari per editim me vlerat ekzistuese
    parametrat = {
        'forma': form,
        'mode': "Modifiko"
    }
    return render(request, 'katalog/templates/form.html', parametrat)
