from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import HttpResponse

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date') or None
        due_time = request.POST.get('due_time') or None

        Task.objects.create(
            title=title,
            due_date=due_date,
            due_time=due_time  # ✅ This line was missing
        )
    return redirect('task_list')
