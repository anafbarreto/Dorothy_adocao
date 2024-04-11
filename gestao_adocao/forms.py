from django import forms
from .models import Adotante, Adocao
from cadastro_animal.models import Animal

class AdotanteForm(forms.ModelForm):
    class Meta:
        model = Adotante
        animal = forms.ModelChoiceField(queryset=Animal.objects.filter(adotado=False), label="Nome do animal", to_field_name='nome')
        fields = ['nome', 'cpf', 'idade', 'telefone', 'email', 'endereco', 'espaco', 'tempo', 'ciente_custos', 'disposicao_fisica_emocional', 'termo_responsabilidade', 'animal_adotado']
        labels = {
            'nome': 'Nome',
            'cpf': 'CPF',
            'idade': 'Idade',
            'telefone': 'Telefone',
            'email': 'Email',
            'endereco': 'Endereço',
            'termo_responsabilidade': 'Aceita o Termo de Responsabilidade acima?',
            'espaco': 'Possui espaço adequado para o animal?',
            'tempo': 'Possui tempo disponível para cuidar do animal?',
            'ciente_custos': 'Está ciente dos custos para manter o animal?',
            'disposicao_fisica_emocional': 'Possui disposição física e emocional para cuidar do animal?',
            'animal_adotado': 'Qual animal deseja adotar?'
        }

class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = ['adotante', 'termo_aceito']
        #fields = ['animais', 'adotante', 'termo_aceito']