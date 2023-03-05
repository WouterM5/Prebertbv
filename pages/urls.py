from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('VeiligheidWelzijn/', views.VeiligheidWelzijn, name='VeiligheidWelzijn'),
    path('juridischeKennisgeving/', views.juridische_kennisgeving, name='juridische_kennisgeving'),

]
