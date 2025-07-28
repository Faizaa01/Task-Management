from django.urls import path
from tasks.views import manager_dashboard,employee_dashboard,delete_task, CreateTask,ViewProject, TaskDetail, dashboard, UpdateTask

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('user-dashboard/', employee_dashboard),
    path('manager-dashboard/', manager_dashboard, name='manager-dashboard'),
    # path('create-task/',create_task, name='create-task'),
    # path('view-task/',view_task),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('update-task/<int:id>/', UpdateTask.as_view(), name='update-task'),
    path('view_task/', ViewProject.as_view(), name='view-task'),
    path('task/<int:task_id>/details/',TaskDetail.as_view(), name='task-details'),


    # path('update-task/<int:id>/',update_task, name='update-task'),
    path('delete-task/<int:id>/',delete_task, name='delete-task'),
    # path('task/<int:task_id>/details/', task_details, name='task-details'),
]