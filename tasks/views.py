from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee,Task,TaskDetails,Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg


def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    return render(request, "test.html")

def create_task(request):
    form = TaskModelForm()
    if request.method == "POST":
        form = TaskModelForm(request.POST)

        if form.is_valid():
            """For Django Model Form"""
            form.save()
            return render(request, 'task_form.html', {"form":form, "message":"Task Added Successfully"})
 
    context = {"form":form}
    return render(request, "task_form.html", context)

def view_task(request):
    tasks = Task.objects.select_related('details').all()
    # tasks = Task.objects.all()
    
    return render(request, "show_task.html",{"tasks":tasks})