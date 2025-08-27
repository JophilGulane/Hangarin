from django.contrib import admin
from .models import Priority, Category, Task, Note, SubTask
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "priority", "category",)
    list_filter = ("status", "priority",)
    search_fields = ("title", "description",)
@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "parent_task_name",)
    search_fields = ("title",)
    list_filter = ("status",)
    def parent_task_name (self, obj):
        try:
            task = SubTask.objects.get(id=obj.parent_task_id)
            return Task.title
        except Task.DoesNotExist:
            return None     
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("task", "content", "created_at",)
    list_filter = ("created_at",)
    search_fields = ("content",)

