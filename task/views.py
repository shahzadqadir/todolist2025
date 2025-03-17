from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from task.models import Meditation, Prayer, Sprint, Task
from .forms import PrayerForm, SprintForm, MeditationForm, TaskForm


def index(request):
    return render(request, 'task/index.html')

@login_required
def tasks(request):
    tasks = Task.objects.filter(owner=request.user).exclude(status='complete')
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



### Meditation Model

class MeditationListView(generic.ListView):
    model = Meditation
    queryset = Meditation.objects.all()
    template_name = 'meditation/meditations.html'
    context_object_name = 'meditations'


class MeditationCreateView(LoginRequiredMixin, generic.CreateView):
    model = Meditation
    form_class = MeditationForm
    template_name = 'meditation/meditation_add.html'
    success_url = reverse_lazy('meditations')


class PrayerListView(generic.ListView):
    model = Prayer
    queryset = Prayer.objects.all()
    template_name = 'prayer/prayers.html'
    context_object_name = 'prayers'


class PrayerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Prayer
    form_class = PrayerForm
    template_name = 'prayer/prayer_add.html'
    success_url = reverse_lazy('prayers')


class SprintListView(generic.ListView):
    model = Sprint
    queryset = Sprint.objects.all()
    template_name = 'sprint/sprints.html'
    context_object_name = 'sprints'


class SprintCreateView(LoginRequiredMixin, generic.CreateView):
    model = Sprint
    form_class = SprintForm
    template_name = 'sprint/sprint_add.html'
    success_url = reverse_lazy('sprints')


class SprintEditView(LoginRequiredMixin, generic.UpdateView):
    model = Sprint    
    form_class = SprintForm
    template_name = 'sprint/sprint_edit.html'
    success_url = reverse_lazy('sprints')
