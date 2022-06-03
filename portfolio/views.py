from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.urls import reverse

from .models import post, PontuacaoQuiz
# Create your views here.
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
    return render(request, 'portfolio/projectos.html')

def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')
def post_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('blog')
    context = {'form': form}

    return render(request, 'portfolio/post.html', context)

def quiz_page_view(request):
    form = PontuacaoQuiz(request.POST or None)
    
    context = {'form': form}

    return render(request, 'portfolio/quiz.html', context)
    
def quizz(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quiz(request)
        r = PontuacaoQuiz(nome=n, pontuacao=p)
        r.save()
def pontuacao_quiz():
    count = 0
    return count
