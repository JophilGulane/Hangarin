"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   
from hangarin.views import HomePageView, TaskList, NoteList, SubTaskList, CategoryList, PriorityList
from hangarin.views import TaskCreateView, NoteCreateView, SubTaskCreateView, CategoryCreateView, PriorityCreateView
from hangarin.views import TaskUpdateView, NoteUpdateView, SubTaskUpdateView, CategoryUpdateView, PriorityUpdateView
from hangarin.views import TaskDeleteView, NoteDeleteView, SubTaskDeleteView, CategoryDeleteView, PriorityDeleteView

from hangarin import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")), # allauth routes
    path('', include('pwa.urls')),
    

    
    path('', HomePageView.as_view(), name='home'),
    
    # Task
    path('task_list/', TaskList.as_view(), name='task-list'),
    path('task_list/add/', TaskCreateView.as_view(), name='task-add'),
    path('task_list/<pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    # Note
    path('note_list/', NoteList.as_view(), name='note-list'),
    path('note_list/add/', NoteCreateView.as_view(), name='note-add'),
    path('note_list/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('note_list/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),

    # SubTask
    path('subtask_list/', SubTaskList.as_view(), name='subtask-list'),
    path('subtask_list/add/', SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtask_list/<int:pk>/', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtask_list/<int:pk>/delete/', SubTaskDeleteView.as_view(), name='subtask-delete'),

    # Category
    path('category_list/', CategoryList.as_view(), name='category-list'),
    path('category_list/add/', CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category_list/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    # Priority
    path('priority_list/', PriorityList.as_view(), name='priority-list'),
    path('priority_list/add/', PriorityCreateView.as_view(), name='priority-add'),
    path('priority_list/<int:pk>/', PriorityUpdateView.as_view(), name='priority-update'),
    path('priority_list/<int:pk>/delete/', PriorityDeleteView.as_view(), name='priority-delete'),
    
]
