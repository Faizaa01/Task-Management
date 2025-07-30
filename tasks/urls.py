from django.urls import path
from tasks.views import manager_dashboard,employee_dashboard, dashboard,view_task, CreateTask, ViewProject, TaskDetail, UpdateTask, DeleteTask

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('user-dashboard/', employee_dashboard, name='employee_dashboard'),
    path('manager-dashboard/', manager_dashboard, name='manager-dashboard'),

    path('view_task/', ViewProject.as_view(), name='view-task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('update-task/<int:id>/', UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:id>/',DeleteTask.as_view(), name='delete-task'),
    path('task/<int:task_id>/details/',TaskDetail.as_view(), name='task-details'),
    path('show-task/',view_task)
]