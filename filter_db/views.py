from django.shortcuts import render
from . import models

from django.views import generic
from .models import Projects,Student

def is_valid_queryparam(param):
    return param != '' and param is not None


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

class StudentCreateView(generic.CreateView) :
    model = models.Student
    template_name = 'student_form.html'
    fields = ['student_id','first_name','middle_name','last_name','start_date','end_date']

class StudentUpdateView(generic.UpdateView) :
    model = models.Student
    template_name = 'student_form.html'
    fields = ['student_id','first_name','middle_name','last_name','start_date','end_date']

class ProjectCreateView(generic.CreateView) :
    model = models.Projects
    template_name = 'project_form.html'
    fields = ['project_id','name', 'start_date', 'end_date','description','students']

class ProjectUpdateView(generic.UpdateView) :
    model = models.Projects
    template_name = 'project_form.html'
    fields = ['project_id','name', 'start_date', 'end_date','description','students']



def BootstrapFilterView(request):
    qs = Projects.objects.all()
    #print('qs',qs)
    name_contains_query = request.GET.get('name_contains')
    description_contains_query = request.GET.get('description_contains')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    student = request.GET.get('student')
    students= Student.objects.all()
    #print(students)


    if name_contains_query != '' and name_contains_query is not None:
        qs = qs.filter(name__icontains=name_contains_query)


    if description_contains_query != '' and description_contains_query is not None:
        qs = qs.filter(description__icontains=description_contains_query)
    
 

    if is_valid_queryparam(date_min) :
        qs = qs.filter(start_date__gte=date_min) 
    
    if is_valid_queryparam(date_max) :
        qs = qs.filter(start_date__lt=date_max) 

    if is_valid_queryparam(student) and student != 'Choose...':
        print('author',student, students)
        qs = qs.filter(students__last_name=student)


    context = {
        'queryset' :qs,
        'students' :students,

    }

    return render(request, "bootstrap_form.html",context)