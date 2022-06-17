"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('blog', views.blog_page_view, name='blog'),
    path('projectos', views.projectos_page_view, name='projectos'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('post', views.post_page_view, name='post'),
    path('quiz', views.quizz, name='quiz'),
    path('login', views.login_page_view, name='login'),
    path('novo_project', views.novo_projects, name='novo_project'),
    path('novo_cadeira', views.novo_cadeira, name='novo_cadeira'),
    path('edita_cadeira/<int:cadeira_id>', views.edita_cadeira_view, name='edita_cadeira'),
    path('apaga_cadeira/<int:cadeira_id>', views.apaga_cadeira_view, name='apaga_cadeira'),
    path('edita_projecto/<int:projecto_id>', views.edita_projecto_view, name='edita_projecto'),
    path('apaga_projecto/<int:projecto_id>', views.apaga_projecto_view, name='apaga_projecto'),
    path('edita_post/<int:post_id>', views.edita_post_view, name='edita_post'),
    path('apaga_post/<int:post_id>', views.apaga_post_view, name='apaga_post'),
    path('logout', views.logout_view, name="logout"),
]