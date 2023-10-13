from django.shortcuts import render
from . import models

from django.views import generic
from .models import Projects


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    all_projects = models.Projects.objects.all()
    return render(request, 'projects.html', {'projects': all_projects} )

def students(request):
    all_students= models.Student.objects.all()
    return render(request, 'students.html', {'students': all_students} )


class ProjectDetailView(generic.DetailView) :
    template_name = 'project_detail.html'
    model = models.Projects
    context_object_name = 'project'


class StudentDetailView(generic.DetailView) :
    template_name = 'student_detail.html'
    model = models.Student
    context_object_name = 'student'

def BootstrapFilterView(request):
    qs = Projects.objects.all()
    name_contains_query = request.GET.get('name_contains')
    # description_contains_query = request.GET.get('description_contains')
    # print(title_contains_query)

    if name_contains_query != '' and name_contains_query is not None:
        qs = qs.filter(name__icontains=name_contains_query)
    context = {
        'queryset' :qs    
    }
    return render(request, "bootstrap_form.html",context)