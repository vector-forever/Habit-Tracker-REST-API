from rest_framework import serializers
from .models import Habitmodel, HabitResponse

# Serializer for Habit model
class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitmodel
        fields = '__all__'

# Serializer for HabitResponse model
class HabitResponseSerializer(serializers.ModelSerializer):
    habit_id = serializers.CharField(source='habit.id', read_only=True)
    class Meta:
        model = HabitResponse
        fields = ['id', 'habit_id', 'date', 'value', 'target']
