from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from cadastro_animal.models import Animal
from cadastro_animal.forms import AnimalForm
from funcionarios.forms import LoginForm

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

def editar_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('pagina_apos_login')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'editar_animal.html', {'form': form})
