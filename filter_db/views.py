from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    all_projects = models.Projects.objects.all()
    return render(request, 'projects.html', {'projects': all_projects} )
