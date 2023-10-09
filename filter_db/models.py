from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(
        primary_key=True,
        unique=True,
        null=False,
        blank=False,
        max_length=50,
    )
    first_name = models.CharField(
        unique=False,
        null=False,
        blank=False,
        max_length=50,

    )
    middle_name = models.CharField(
        unique=False,
        null=True,
        blank=True,
        max_length=50,

    )
    last_name = models.CharField(
        unique=False,
        null=False,
        blank=False,
        max_length=50,

    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.last_name
    

class Projects(models.Model):

    student_id = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50,    
    )
    project_id = models.CharField(
        primary_key= True,
        unique = False,
        null = False,
        blank = False,
        max_length=50,
    )
    name = models.TextField(
        unique = False,
        null = False,
        blank = False,
        max_length=2000,
    )
    start_date = models.DateField()

    end_date = models.DateField()
    
    description = models.TextField(
        unique = False,
        null = False,
        blank = False,
        max_length=5000,
    )
    
    students = models.ManyToManyField(
        Student,
        related_name='students'
    )

    def __str__(self) -> str:
        return self.name
