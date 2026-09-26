from django.shortcuts import render

def atracoes(request):
    """Renderiza a página com as principais atrações turísticas de Salvador."""
    return render(request, 'meudestino/atracoes.html')

def historia(request):
    """Renderiza a página sobre a história e cultura da cidade."""
    return render(request, 'meudestino/historia.html')

def galeria(request):
    """Renderiza a galeria de imagens e monumentos de Salvador."""
    return render(request, 'meudestino/galeria.html')