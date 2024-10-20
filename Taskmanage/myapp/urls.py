from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView,TaskRetrieveUpdateDestroyView
from.views import*




urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'), # List all tasks
    path('create/', TaskCreateView.as_view(), name='task-create'),    # Create a new task
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('api/update/tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('api/delete/tasks/<int:pk>/', TaskDeleteView.as_view(), name='task-delete')
    
]