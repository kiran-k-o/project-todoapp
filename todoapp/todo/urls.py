from django.urls import path, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from .views import TaskCreate, RegisterView, TaskList, CustomLoginView, TaskDetailView, TaskUpdate, TaskDelete

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

urlpatterns = [
    path('', TaskCreate.as_view(), name='createtask'),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('tasks/', TaskList.as_view(), name='task'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('task-details/<int:pk>/', TaskDetailView.as_view(), name='details'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='delete')
]

