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
    task = Task.objects.all()
    return render(request, 'index.html', {'tacks': task})

def create_task(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'create.html', {'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        title = request.POST.get('title')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        content = request.POST.get('content')
        new_task = Task.objects.create(title=title, status=status, content=content, deadline=deadline)
        #return render(request, 'task_view.html', {'task': new_task})
       # url = reverse('task_view', kwargs={'pk':new_task.pk})
       # return HttpResponseRedirect(url)
    return redirect('task_view', pk=new_task.pk)


def task_view(request, pk, *args, **kwargs):
#    task_id = kwargs.get('pk')
#    task = Task.objects.get(pk=task_id)
#    try:
 #       task = Task.objects.get(pk=pk)
  #  except Task.DoesNotExist:
#        return HttpResponseNotFound('Not Found')
  #      raise Http404
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)

