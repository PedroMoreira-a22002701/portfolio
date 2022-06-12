from imaplib import _Authenticator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm, Project, Cadeira
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt

from .models import post, PontuacaoQuiz, cadeira, projecto
from django.shortcuts import render
from django.http import HttpResponse

def portfolio_view(request):
    return render(request, 'portfolio/layout.html')

def home_page_view(request):
    return render(request, 'portfolio/home.html')

def blog_page_view(request):
    context = {'portfolio': post.objects.all()}
    return render(request, 'portfolio/blog.html', context)

def projectos_page_view(request):
    context = {'portfolio': projecto.objects.all()}
    return render(request, 'portfolio/projectos.html', context)

def licenciatura_page_view(request):
    context = {'portfolio': cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)
def login_page_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('licenciatura')
        else:
            return render(request, "portfolio/login.html", {
                'message': "Invalid credentials."
            })
    return render(request, 'portfolio/login.html')    
    
def post_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('blog')
    context = {'form': form}

    return render(request, 'portfolio/post.html', context)



def quizz(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = pontuacao_quiz(request)
        r = PontuacaoQuiz(nome=n, pontos=p)
        r.save()
        return render(request, 'portfolio/quiz.html')
    context = {'data': desenha_grafico_resultados()}    
    return render(request, 'portfolio/quiz.html',context)    

def pontuacao_quiz(request):
    count = 0
    if(request.POST['0'] == 'HyperText Markup Language'):
        count = count + 1
    if(request.POST['1'] == 'Cascading Style Sheet'):
        count = count + 1
    if(request.POST['2'] == 'box-shadow: 10px 10px 5px grey;'):
        count = count + 1    
    if(request.POST['3'] == 'text-wrap: break-word;'):
        count = count + 1   
    if(request.POST['4'] == 'border-radius: 30px;'):
        count = count + 1             
    return count
def desenha_grafico_resultados():
    pontuacoes = PontuacaoQuiz.objects.all()
    pontuacao_sorted = sorted(pontuacoes, key=lambda objeto: objeto.pontos, reverse=False)
    lista_nomes = []
    lista_pontuacao = []

    for person in pontuacao_sorted:
        lista_nomes.append(person.nome)
        lista_pontuacao.append(person.pontos)

    plt.barh(lista_nomes, lista_pontuacao)
    plt.savefig('portfolio/static/portfolio/images/graf.png', bbox_inches='tight')

@login_required
def edit_projects(request):
    form = Project(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projectos'))

    context = {'form': form}

    return render(request, 'portfolio/edit_project.html', context)
    
@login_required
def edit_cadeira(request):
    form = Cadeira(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('licenciatura')
    context = {'form': form}

    return render(request, 'portfolio/edit_cadeira.html', context)    
    