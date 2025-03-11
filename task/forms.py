from django import forms

from .models import Sprint, Task, Prayer, Meditation


class SprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ['name', 'due_date', 'status', 'comments', 'prize_earned']


class PrayerForm(forms.ModelForm):
    class Meta:
        model = Prayer
        fields = ('date_prayed', 'comments', 'sprint')


class MeditationForm(forms.ModelForm):
    class Meta:
        model = Meditation
        fields = ('date_meditated', 'minutes_spent', 'comments', 'sprint')


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('owner', )


