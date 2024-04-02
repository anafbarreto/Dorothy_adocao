from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Animal

class LoginForm(AuthenticationForm):
    pass

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'especie', 'idade', 'descricao']
        # Adicione mais campos conforme necessário
