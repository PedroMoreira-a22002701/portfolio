from django.forms import ModelForm

from .models import cadeira, projecto,  post

class PostForm(ModelForm):
    class Meta:
        model = post
        fields = '__all__'

class Project(ModelForm):
    class Meta:
        model = projecto
        fields = '__all__'

class Cadeira(ModelForm):
    class Meta:
        model = cadeira
        fields = '__all__'        