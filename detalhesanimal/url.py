from django.urls import path
from detalhesanimal.views import detalhes_animal

app_name = 'detalhesanimal'
urlpatterns = [
    path('animal/<int:animal_id>/', detalhes_animal, name='detalhes_animal'),
]
