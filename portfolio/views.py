from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def portfolio_view(request):
    return render(request, 'portfolio/layout.html')

def home_page_view(request):
    return render(request, 'portfolio/home.html')

def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentacao.html')

def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')

def formacao_page_view(request):
    return render(request, 'portfolio/formacao.html')

def projectos_page_view(request):
    return render(request, 'portfolio/projectos.html')

def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')