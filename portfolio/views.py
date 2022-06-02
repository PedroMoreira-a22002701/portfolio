from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.urls import reverse
from .models import post
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
    form = PostForm()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio/blog.html'))
    context = {'form': form}

    return render(request, 'portfolio/post.html', context)