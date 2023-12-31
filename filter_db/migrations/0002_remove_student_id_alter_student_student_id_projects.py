# Generated by Django 4.2.6 on 2023-10-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('project_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=2000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(max_length=5000)),
                ('students', models.ManyToManyField(related_name='students', to='filter_db.student')),
            ],
        ),
    ]
