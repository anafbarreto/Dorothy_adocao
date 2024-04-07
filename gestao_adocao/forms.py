from banco.models import adocao
from django import forms

class AdocaoForm(forms.ModelForm):
    class Meta:
        model = adocao
        fields = ['animais', 'adotante', 'termo_aceito']