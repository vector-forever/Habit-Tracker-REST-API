from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Habitmodel, HabitResponse
from .serializers import HabitSerializer, HabitResponseSerializer

# create and list habits
class Habitlistcreate(generics.ListCreateAPIView):
    queryset = Habitmodel.objects.all()
    serializer_class = HabitSerializer

# update and delete habits
class Habitupdatedelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitmodel.objects.all()
    serializer_class = HabitSerializer

# create and list responses for a habit
class HabitResponseListCreate(generics.ListCreateAPIView):
    queryset = HabitResponse.objects.all()
    serializer_class = HabitResponseSerializer

    def get_queryset(self):
        return self.queryset.filter(habit_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        habit = get_object_or_404(Habitmodel, pk=self.kwargs['pk'])
        serializer.save(habit_id=habit)

# update and delete responses for a habit
class HabitResponsedelup(generics.RetrieveUpdateDestroyAPIView):
    queryset = HabitResponse.objects.all()
    serializer_class = HabitResponseSerializer

    def get_queryset(self):
        return self.queryset.filter(habit_id=self.kwargs['habit_pk'], pk=self.kwargs['pk'])