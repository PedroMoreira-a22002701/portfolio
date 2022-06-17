from imaplib import _Authenticator
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm, Project, Cadeira
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import base64
import io
import urllib


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
def logout_view(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'Desconectado.'
    })     
    
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
    pontuacoes = PontuacaoQuiz.objects.all().order_by('pontos')

    listaNomes = [pontuacao.nome for pontuacao in pontuacoes]
    listaPontuacao = [pontuacao.pontos for pontuacao in pontuacoes]

    plt.barh(listaNomes, listaPontuacao)
    plt.ylabel("Pontuacao")
    plt.autoscale()

    fig = plt.gcf()
    plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')

    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri
@login_required
def edita_post_view(request, post_id):
    posts = post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=posts)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita_post.html', context)

def apaga_post_view(request, post_id):
    post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

@login_required
def novo_projects(request):
    form = Project(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projectos'))

    context = {'form': form}

    return render(request, 'portfolio/novo_project.html', context)
    
@login_required
def novo_cadeira(request):
    form = Cadeira(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('licenciatura')
    context = {'form': form}

    return render(request, 'portfolio/novo_cadeira.html', context)    
    
@login_required
def edita_cadeira_view(request, cadeira_id):
    cadeiras = cadeira.objects.get(id=cadeira_id)
    form = Cadeira(request.POST or None, instance=cadeiras)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'portfolio/edita_cadeira.html', context)

@login_required
def apaga_cadeira_view(request, cadeira_id):
    cadeira.objects.get(id=cadeira_id).delete()
    return HttpResponseRedirect(reverse('portfolio:licenciatura'))
@login_required
def edita_projecto_view(request, projecto_id):
    projectos = projecto.objects.get(id=projecto_id)
    form = Project(request.POST or None, instance=projectos)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projectos'))

    context = {'form': form, 'projecto_id': projecto_id}
    return render(request, 'portfolio/edita_projecto.html', context)

@login_required
def apaga_projecto_view(request, projecto_id):
    projecto.objects.get(id=projecto_id).delete()
    return HttpResponseRedirect(reverse('portfolio:projectos'))