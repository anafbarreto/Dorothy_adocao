from django import forms
from django.contrib.auth.forms import AuthenticationForm
from funcionario.models import funcionarios
from django.contrib.auth.hashers import make_password

class LoginForm(AuthenticationForm):
    pass

class CadastroFuncionarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = funcionarios
        fields = ['nome','email','cargo','usuario','senha']
        
    def save(self, commit=True):
        # Obtém a senha não criptografada do formulário
        senha = self.cleaned_data.get('senha')
        
        # Criptografa a senha antes de salvar o objeto Cadastro
        if senha:
            self.instance.senha = make_password(senha)
        
        return super().save(commit)