from django import forms
from .models import funcionarios

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = funcionarios
        fields = '__all__'
