from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from task.models import Task

from .forms import PrayerForm, SprintForm, MeditationForm


def index(request):
    return render(request, 'tasks/index.html')

@login_required
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task/tasks.html', {'tasks': tasks})


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