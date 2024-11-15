from django.shortcuts import render
from .models import *




# Create your views here.
from django.views.generic import ListView
class Tasklistviews(ListView):
    model =  blogmodel
    template_name = 'home.html'
    context_object_name = 'dict1'
    ordering =['-created_at']

from django.views.generic.detail import DetailView
class TaskDetailviews(DetailView):
    model = blogmodel
    template_name = 'detail.html'
    context_object_name = 'dict2'

from django.views.generic.edit import DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy
class TaskDeleteView(DeleteView):
    model =blogmodel
    template_name = 'delete.html'  # Template to confirm deletion
    success_url = reverse_lazy('home')  # Redirect to home after deletion

class TaskCreateView(CreateView):
    model = blogmodel
    template_name = 'Post.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
class TaskUpdateView(UpdateView):
    model = blogmodel
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
