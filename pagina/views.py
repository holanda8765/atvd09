from django.shortcuts import render, get_object_or_404
from .models import Conteudo, Menu

def obter_menu():
    return Menu.objects.filter(ativo=True).order_by('ordem') # obtenção dos itens do menu

def pagina_inicial(request):
    menu = obter_menu()
    # A página inicial pode ser um conteúdo específico definido por um slug padrão, ex: 'inicio'
    conteudo = get_object_or_404(Conteudo, slug='inicio', ativo=True)
    return render(request, 'base.html', {'conteudo': conteudo, 'menu': menu}) # página inicial[cite: 8]

def exibir_conteudo(request, slug):
    menu = obter_menu()
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, 'base.html', {'conteudo': conteudo, 'menu': menu}) # apresentação de um conteúdo específico[cite: 8]