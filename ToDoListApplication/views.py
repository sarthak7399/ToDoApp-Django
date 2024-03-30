from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    # return HttpResponse("Hello World!")
    tasks=Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'tasks':tasks, 'form':form}
    return render(request, 'ToDoListApplication/list.html', context=context)

def updateTask(request, pk):    # pk is primary key
    task=Task.objects.get(id=pk)

    form=TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'form':form}

    return render(request, 'ToDoListApplication/update_task.html', context=context)


def deleteTask(request, pk):
    item=Task.objects.get(id=pk)
    context={'item':item}

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, "ToDoListApplication/delete.html", context=context)