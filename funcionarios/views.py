from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from cadastro_animal.models import Animal
from cadastro_animal.forms import AnimalForm
from funcionarios.forms import LoginForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from funcionarios.forms import CadastroFuncionarioForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pagina_apos_login')
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def pagina_apos_login(request):
    animais = Animal.objects.all()
    return render(request, 'pagina_apos_login.html', {'animais': animais})

def excluir_animal(request, animal_id):
    if request.method == 'POST':
        animal = get_object_or_404(Animal, pk=animal_id)
        animal.delete()
        return HttpResponseRedirect(reverse('pagina_apos_login')) 
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)


def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('pagina_apos_login')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'editar_animal.html', {'form': form})

def cadastro_funcionario(request):
    sucess = False
    if(request.method=='GET'):
        form = CadastroFuncionarioForm()
    else:
        form = CadastroFuncionarioForm(request.POST)
        if form.is_valid():
            sucess = True
            form.save()
    context = {
    'form':form,
    'sucess':sucess
    }
    return render(request,'cadastro.html', context);
