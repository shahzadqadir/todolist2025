from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from task.models import Task

from .forms import PrayerForm, SprintForm, MeditationForm, TaskForm


def index(request):
    return render(request, 'task/index.html')

@login_required
def tasks(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'task/tasks.html', {'tasks': tasks})

@login_required
def task_add(request):
    form = TaskForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = TaskForm(request.POST)
        candidate = form.save(commit=False)
        candidate.owner = request.user
        candidate.save()
        return redirect('tasks')
    return render(request, 'task/task_add.html', context)


@login_required
def task(request, id):
    task = Task.objects.get(pk=id)
    context = {
        'task': task,
    }
    return render(request, 'task/task.html', context)

@login_required
def task_edit(request, id):
    task = Task.objects.get(pk=id)
    
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        
    context = {
        'form': form
    }
    
    return render(request, 'task/task_edit.html', context)

@login_required
def task_delete(request, id):
    task = Task.objects.filter(owner=request.user).get(pk=id)
    context = {
        'task': task,
    }
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'task/task_delete.html', context)

@login_required
def add_sprint(request):
    if request.method == 'GET':
        form = SprintForm()
    return render(request, 'task/add_sprint.html', {'form': form})


@login_required
def add_prayer(request):
    if request.method == 'GET':
        form = PrayerForm()
    return render(request, 'task/add_prayer.html', {'form': form})


@login_required
def add_meditation(request):
    if request.method == 'GET':
        form = MeditationForm()
    return render(request, 'task/add_meditation.html', {'form': form})