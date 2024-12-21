from . import views
from django.urls import path

urlpatterns = [
    path('todo/',views.todo_list,name='todo_list'),
]
