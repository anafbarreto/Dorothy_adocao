from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from banco.models import cadastro_animais

# Create your views here.
def detalhes_animal(request, animal_id):
    animal = get_object_or_404(cadastro_animais, pk=animal_id)
    return render(request, 'detalhes_animal.html', {'animal': animal})

