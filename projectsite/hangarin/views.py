from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from hangarin.models import Category, Task, SubTask, Note, Priority
from projectsite.hangarin.forms import TaskForm, NoteForm, SubTaskForm, PriorityForm, CategoryForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView



class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = "account_login"  # name of your signin URL
    redirect_field_name = "next"  # optional
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Summary counts
        context["total_task"] = Task.objects.count()
        context["total_note"] = Note.objects.count()
        context["total_subtask"] = SubTask.objects.count()
        context["total_category"] = Category.objects.count()
        context["total_priority"] = Priority.objects.count()

        # Extra context for dashboard
        today = timezone.now().date()

        # Show tasks with deadlines in the next 7 days
        context["near_deadline_tasks"] = Task.objects.filter(deadline__gte=today, deadline__lte=today + timezone.timedelta(days=7)).order_by("deadline")

        # Show most recent tasks (e.g. last 5 created)
        context["recent_tasks"] = Task.objects.order_by("-created_at")[:5]

        return context

    
# -------------------- Task --------------------
class TaskList(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5
    ordering = ["title","description"]
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter( 
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(deadline__icontains=query) |
                Q(status__icontains=query)
                ) 
        return qs 
    
    def get_ordering(self):
        allowed = ["title", "deadline", "status"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "title"

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

# -------------------- Note --------------------
class NoteList(ListView):
    model = Note
    context_object_name = 'note'
    template_name = 'note_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter( 
                Q(task__title__icontains=query) |
                Q(content__icontains=query)
                ) 
        return qs 
    
    def get_ordering(self):
        allowed = ["task", "content",]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "task"

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')

# -------------------- SubTask --------------------
class SubTaskList(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = 'subtask_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter( 
                Q(parent_task__title__icontains=query) |
                Q(title__icontains=query) |
                Q(status__icontains=query)
                ) 
        return qs 
    
    def get_ordering(self):
        allowed = ["parent_task","title", "status",]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "title"

class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')

# -------------------- Category --------------------
class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter( 
                Q(name__icontains=query)
                ) 
        return qs 

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

# -------------------- Priority --------------------
class PriorityList(ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = 'priority_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter( 
                Q(name__icontains=query)
                ) 
        return qs 

class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')
