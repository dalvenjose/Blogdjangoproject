from django.urls import  path
from .views import *


urlpatterns = [
    
    path('',Tasklistviews.as_view(),name='home'),
    path('detail/<int:pk>',TaskDetailviews.as_view(),name='detail1'),
     path('post/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'), 
     path('post/new/', TaskCreateView.as_view(), name='task_create'),
     path('post/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update')
]
