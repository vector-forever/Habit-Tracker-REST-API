from django.db import models
from django.contrib.auth.models import User

class Habitmodel(models.Model):
    # Choices for habit type
    TYPE_CHOICES = [
        ('yesorno', 'Yes or No'),
        ('measurable', 'Measurable'),
    ]
    
    # Fields for the Habitmodel
    title = models.CharField(max_length=255)
    question = models.CharField(max_length=400, default='')
    habit_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    target = models.PositiveIntegerField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HabitResponse(models.Model):
    # Choices for value field
    TYPE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    # Fields for the HabitResponse model
    habit_id = models.ForeignKey(Habitmodel, on_delete=models.CASCADE)
    value = models.CharField(max_length=10, choices=TYPE_CHOICES, default='No', blank=True, null=True)
    target = models.PositiveIntegerField(default=None, blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Make habit_id and date fields unique together
    class Meta:
        unique_together = ['habit_id', 'date']
