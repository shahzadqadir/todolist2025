from django.contrib import admin

from .models import Task, Prayer, Meditation, Sprint


class SprintAdmin(admin.ModelAdmin):
    model = Sprint
    list_display = ['name', 'due_date', 'status', 'comments']


class PrayerAdmin(admin.ModelAdmin):
    model = Prayer
    list_display = ('date_prayed', 'comments', 'sprint')

class MeditationAdmin(admin.ModelAdmin):
    model = Meditation
    list_display = ('date_meditated', 'minutes_spent', 'comments', 'sprint')

class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('description', 'due_date', 'official_due_by', 'late_fine', 'priority', 'status')

admin.site.register(Sprint, SprintAdmin)
admin.site.register(Prayer, PrayerAdmin)

admin.site.register(Meditation, MeditationAdmin)
admin.site.register(Task, TaskAdmin)
