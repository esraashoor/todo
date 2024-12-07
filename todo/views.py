from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    # print(request.POST['task'])
    task = request.POST['task']
    Task.objects.create(task=task)
    # return HttpResponse('The form is supmited')
    return redirect('home')