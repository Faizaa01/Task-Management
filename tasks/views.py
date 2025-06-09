from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # work with database,transform data, data pass, https reponse/json response
    return HttpResponse("Welcome to Task Management System")

def contact(request):
    return HttpResponse("<h1 style='color: pink'>This is contact page</h1>")

def show_task(request):
    return HttpResponse("This is our task page")

def show_specific_task(request, id):
    print("id ", id)
    print("id type", type(id))
    return HttpResponse(f"This is specific task page {id}")