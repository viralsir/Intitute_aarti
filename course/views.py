from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import course_master
# Create your views here.
class NewCourse(CreateView):
    model = course_master
    fields = '__all__'

# model_form.html
#course_master_form.html
