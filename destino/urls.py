from django.urls import path
from . import views

urlpatterns = [
    path('', views.atracoes, name='atracoes'),
    path('historia/', views.historia, name='historia'),
    path('galeria/', views.galeria, name='galeria'),
]