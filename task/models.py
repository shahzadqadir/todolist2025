from django.db import models
from django.contrib.auth import get_user_model

from django.utils import timezone



class Sprint(models.Model):
    STATUS_CHOICES = [('notdone', 'notdone'), ('inprogress', 'inprogress'), ('done', 'done')]
    name = models.CharField(max_length=255)
    due_date = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=255)
    comments = models.TextField()
    prize_earned = models.BooleanField(default=False)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIO_CHOICES = [('high', 'high'), ('medium', 'medium'), ('low', 'low')]
    description = models.CharField(max_length=1000)
    due_date = models.DateField(blank=True, null=True)
    date_completed = models.DateField(null=True, blank=True)
    official_due_by = models.DateField(null=True, blank=True)
    late_fine = models.IntegerField(null=True, blank=True, default=0)
    priority = models.CharField(choices=PRIO_CHOICES, max_length=255)
    comments = models.TextField(null=True, blank=True)
    task_img = models.ImageField(null=True, blank=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(choices=[
        ('notdone', 'notdone'), 
        ('inprogress', 'inprogress'), 
        ('complete', 'complete')], 
        max_length=255, blank=True, null=True)

    def __str__(self):
        return self.description[:50]
    

class Prayer(models.Model):
    date_prayed = models.DateField()
    comments = models.TextField(null=True, blank=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"Prayer: {self.comments}"
    

class Meditation(models.Model):
    date_meditated = models.DateField()
    minutes_spent = models.IntegerField(default=0)
    comments = models.TextField()
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"Mediation: {str(self.minutes_spent)} minutes."