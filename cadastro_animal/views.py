import cadastro_animal.views
import uuid
from django.shortcuts import render
from cadastro_animal.models import Animal
from cadastro_animal.forms import AnimalForm
from rest_framework import viewsets
from cadastro_animal.serializers import AnimalSerializer
from django.db.models import Q
# Create your views here.

def home(request):
   # Filtrar apenas os animais que não foram adotados
    list_animals = Animal.objects.filter(adotado=False)
  
    return render(request, 'home.html',{'list_animals':list_animals});



def pesquisa_animal(request):
    query = request.GET.get('q')
    list_animals = Animal.objects.filter(
        Q(nome__icontains=query) | 
        Q(especie__icontains=query) |
        Q(raca__icontains=query)|
        Q(porte__icontains=query)|
         Q(idade__icontains=query)|
        Q(sexo__icontains=query)
       
    ) if query else Animal.objects.filter(adotado=False)
    mensagem = None

    if query and not list_animals:
        mensagem = f"Parametro de busca '{query}' inválido."

    return render(request, 'home.html', {'list_animals': list_animals, 'mensagem': mensagem, 'query': query})

def criar_animal(request):
    sucess = False  # Inicialmente, definimos sucesso como falso
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.id = uuid.uuid4()
            animal.save()
            sucess = True  # Definimos sucesso como verdadeiro após salvar com sucesso
            # Limpar o formulário após salvar
            form = AnimalForm()
    else:
        form = AnimalForm()
    
    return render(request, 'cadastro.html', {'form': form, 'sucess': sucess})

#! O AnimalSerializer é uma classe que converte objetos Animal em formatos como JSON para serem enviados pela API e vice-versa.
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    
# Com essa configuração,voce consegue fazer as operações CRUD padrão para o modelo Animal . Isso inclui criar, recuperar, atualizar e excluir objetos Animal através da API REST.
