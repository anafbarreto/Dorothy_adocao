from django.shortcuts import render
from gestao_adocao.forms import AdotanteForm
#Aqui ainda tenho que adaptar para pegar da pagina de detalhes
#def inicio(request):
#return render(request, 'inicio.html')

def adocao(request):
    sucesso = False  # Define uma flag de sucesso como falso inicialmente
    form = AdotanteForm(request.POST or None)  # Cria uma instância do formulário AdotanteForm

    if form.is_valid():  # Verifica se o formulário é válido
        sucesso = True  # Se for válido, define a flag de sucesso como verdadeiro
        form.save()  # Salva os dados do formulário

    contexto = {  # Cria um contexto para passar para o template
        'form': form,  # Passa o formulário
        'sucesso': sucesso  # Passa a flag de sucesso
    }

    return render(request, 'adocao.html', contexto)  # Renderiza o template adocao.html com o contexto
