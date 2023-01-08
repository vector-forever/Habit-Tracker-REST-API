from django.urls import path
from . import views

urlpatterns = [
    path('habits/', views.Habitlistcreate.as_view(), name='habit-list'),
    path('habits/<int:pk>/', views.Habitupdatedelete.as_view(), name='habit-del_upd'),
    path('habits/response/<int:pk>/', views.HabitResponseListCreate.as_view(), name='habit-response-create'),
    path('habits/response/<int:habit_pk>/update/<int:pk>/', views.HabitResponsedelup.as_view(), name='habit-response-update'),
]


