# from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

    completed_tasks = Task.objects.filter(is_completed=True)
    print(completed_tasks)

    # print(tasks)
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }
    # return HttpResponse('<h1>This is my home page</h1>')
    return render(request, 'home.html', context)