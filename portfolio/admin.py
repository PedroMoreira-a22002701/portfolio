from django.contrib import admin
from .models import post
from .models import PontuacaoQuiz , cadeira, projecto
# Register your models here.
admin.site.register(post)
admin.site.register(PontuacaoQuiz)
admin.site.register(cadeira)
admin.site.register(projecto)