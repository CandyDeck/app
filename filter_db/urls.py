## APP(filter_db)

from django.urls import path
from . import views
from filter_db.views import BootstrapFilterView


urlpatterns = [
    path('', views.index, name ='index'),
    path('about',views.about,name='about'),
    path('projects/',views.projects,name='projects'),
    path('project/<str:pk>', views.ProjectDetailView.as_view(),name = 'project_detail'),
    path('students',views.students,name='students'),
    path('student/<str:pk>', views.StudentDetailView.as_view(),name = 'student_detail'),
    path('bootstrap/', BootstrapFilterView,name = 'bootstrap_form'),

]