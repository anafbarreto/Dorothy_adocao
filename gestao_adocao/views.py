from django.shortcuts import render, redirect
from .forms import AdocaoForm

def adocao_create(request):
    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            adocao_instance = form.save()
            # Redirect to a success page or do something else
            return redirect('success_url_name')  # Replace 'success_url_name' with the name of your success URL
    else:
        form = AdocaoForm()
    return render(request, 'adocao_form.html', {'form': form})
