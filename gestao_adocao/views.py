from django.shortcuts import render
from gestao_adocao.forms import AdocaoForm
#Aqui ainda tenho que adaptar para pegar da pagina de detalhes
def inicio(request):
    return render(request, 'inicio.html')

def adocao(request):
    sucesso = False 
    if request.method == 'GET':
        form = AdocaoForm()
    else:
        form = AdocaoForm(request.POST)
        if form.is_valid():
            sucesso = True 
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'adocao.html', contexto)
