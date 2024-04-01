"""
URL configuration for projeto_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from detalhesanimal.views import detalhes_animal
from django.conf.urls.static import static
from django.conf import settings
from detalhesanimal.views import detalhes_animal
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detalhes_animal/', detalhes_animal, name='detalhes_animal')
#    path('detalhes_animal/<int:animal_id>/', detalhes_animal, name='detalhes_animal'),  /* teste com uma imagem - - - apagar
#    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
