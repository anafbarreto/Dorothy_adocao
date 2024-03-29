import uuid
from django.shortcuts import render
from cadastro_animal.models import Animal
from cadastro_animal.forms import AnimalForm
from rest_framework import viewsets
from cadastro_animal.serializers import AnimalSerializer

def criar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
             # Gerar UUID automaticamente
            animal.id = uuid.uuid4()
            animal.save()
            form = AnimalForm()  # Limpar o formulário após salvar
    else:
        form = AnimalForm()
    return render(request, 'cadastro.html', {'form': form})

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
# Create your views here.
