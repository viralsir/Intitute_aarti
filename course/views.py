from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import course_master
# Create your views here.
class NewCourse(CreateView):
    model = course_master
    fields = '__all__'


# model_form.html
#course_master_form.html

class ViewCourse(ListView):
    model = course_master
    context_object_name = 'courses'

class UpdateCourse(UpdateView):
    model = course_master
    fields = '__all__'
