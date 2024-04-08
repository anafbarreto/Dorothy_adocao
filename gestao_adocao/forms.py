from django import forms
from .models import Adotante, Adocao

class AdotanteForm(forms.ModelForm):
    class Meta:
        model = Adotante
        fields = ['nome', 'cpf', 'idade', 'telefone', 'email', 'endereco', 'termo_responsabilidade', 'espaco', 'tempo', 'ciente_custos', 'disposicao_fisica_emocional']
        labels = {
            'nome': 'Nome',
            'cpf': 'CPF',
            'idade': 'Idade',
            'telefone': 'Telefone',
            'email': 'Email',
            'endereco': 'Endereço',
            'termo_responsabilidade': 'Termo de Responsabilidade',
            'espaco': 'Possui espaço adequado para o animal?',
            'tempo': 'Possui tempo disponível para cuidar do animal?',
            'ciente_custos': 'Está ciente dos custos para manter o animal?',
            'disposicao_fisica_emocional': 'Possui disposição física e emocional para cuidar do animal?'
        }

class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = ['adotante', 'termo_aceito']
        #fields = ['animais', 'adotante', 'termo_aceito']