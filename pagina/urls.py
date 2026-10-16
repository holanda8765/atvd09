from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='home'), # uma URL para a página inicial[cite: 7]
    path('conteudo/<slug:slug>/', views.exibir_conteudo, name='conteudo_detalhe'), # uma URL dinâmica para exibição dos conteúdos[cite: 7]
]