from django.shortcuts import render, redirect
from .models import *
from .forms import *

#Task list and form to create a new task
def listTask(request):
    queryset = task.objects.order_by('completed', 'due')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)    
        if form.is_valid():
            form.save()
        return redirect('/')
    #renders data from DB
    context = {
        'tasks':queryset,
        'form':form,
    }
    return render(request, 'list_task.html', context)

#Update the task by primary key (pk)
def updateTask(request, pk):
    queryset = task.objects.get(id=pk)
    form = UpdateForm(instance=queryset)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/')
    #render the updated data for display
    context = {
        'form':form
    }
    return render(request, 'update_task.html', context)

#user can delete a task
def deleteTask(request, pk):
    queryset = task.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/')
    context = {
        'item':queryset
    }
    return render(request, 'delete_task.html', context)    