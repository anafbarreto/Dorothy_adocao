from django import forms

class AdocaoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cpf = forms.CharField(label='CPF', max_length=11, min_length=11)
    idade = forms.IntegerField(label='Idade')
    endereco = forms.CharField(label='Endereço', max_length=255)
    telefone = forms.CharField(label='Telefone', max_length=20)
    email = forms.EmailField(label='Email')
    espaco = forms.BooleanField(label='Possui espaço adequado para o animal?', required=False)
    tempo = forms.BooleanField(label='Possui tempo disponível para cuidar do animal?', required=False)
    ciente_custos = forms.BooleanField(label='Está ciente dos custos para manter o animal?', required=False)
    disposicao = forms.BooleanField(label='Possui disposição física e emocional para cuidar do animal?', required=False)
    data_adoção = forms.DateTimeField(label='Data da adoção')

    def clean_idade(self):
        idade = self.cleaned_data['idade']
        if idade < 18:
            raise forms.ValidationError("Você deve ter pelo menos 18 anos para adotar um pet.")
        return idade

    def clean(self):
        cleaned_data = super().clean()
        espaco = cleaned_data.get("espaco")
        tempo = cleaned_data.get("tempo")
        ciente_custos = cleaned_data.get("ciente_custos")
        disposicao = cleaned_data.get("disposicao")

        if not all([espaco, tempo, ciente_custos, disposicao]):
            raise forms.ValidationError(
                "Você não possui as características necessárias para realizar a adoção"
            )