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



def quizz(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = pontuacao_quiz(request)
        r = PontuacaoQuiz(nome=n, pontos=p)
        r.save()
        return render(request, 'portfolio/quiz.html')
    return render(request, 'portfolio/quiz.html')    

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
