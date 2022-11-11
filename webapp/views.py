from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
# Create your views here.

def index_view(request, *args, **kwargs):
    if request.method == "POST":
        task_id = request.GET.get('id')
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('index')
    task = Task.objects.all()
    return render(request, 'index.html', {'tacks': task})

def create_task(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'create.html', {'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        title = request.POST.get('title')
        status = request.POST.get('status')
        content = request.POST.get('content')
        deadline = request.POST.get('deadline')
        if not deadline:
            deadline = None
        new_task = Task.objects.create(title=title, status=status, content=content, deadline=deadline)

    return redirect('task_view', pk=new_task.pk)


def task_view(request, pk, *args, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)

def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_update.html', {'task': task})
    elif request.method == "POST":
        task.title = request.POST.get('title')
        task.status = request.POST.get('status')
        task.content = request.POST.get('content')
        task.deadline = request.POST.get('deadline')
        task.save()
        return redirect('task_view', pk=task.pk)



