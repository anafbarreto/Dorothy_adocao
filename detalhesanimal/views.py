from django.shortcuts import render, get_object_or_404
from .models import cadastro_animais
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def detalhes_animal(request, animal_id):
    # Obter o objeto Animal com base no animal_id
    animal = get_object_or_404(cadastro_animais, pk=animal_id)
    return render(request, 'detalhes_animal.html', {'animal': animal})
    # Aqui você pode passar qualquer informação adicional relacionada ao animal para o template
    # Por exemplo, você pode querer obter informações adicionais relacionadas a esse animal ou realizar outras operações relacionadas a ele

    


