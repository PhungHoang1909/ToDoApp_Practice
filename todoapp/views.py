from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from .models import todoModel

# return homepage
def homepage(request):
    todos = todoModel.objects.all()
    return render(request, 'base.html', {'todos': todos })

# Add Tasks
@require_http_methods(['POST'])
def add_task(request):
    actions = None  # Renamed variable to maintain consistency
    task_title = request.POST.get('task_title', "")

    if task_title:
        actions = todoModel.objects.create(task_title=task_title)

    return render(request, 'actions/actions.html', {'actions': actions})

# Mark as done
@require_http_methods(['PUT'])
def update_task(request, pk):
    actions = todoModel.objects.get(pk=pk)
    actions.is_done = True
    actions.save()

    return render(request, 'actions/actions.html', {'actions': actions})

# Delete tasks
@require_http_methods(['DELETE'])
def delete_task(request, pk):
    actions = todoModel.objects.get(pk = pk)
    
    actions.delete()

    return HttpResponse()

# edit Tasks
@require_http_methods(['GET', 'POST'])
def edit_task(request, pk):
    actions = todoModel.objects.get(pk = pk)

    if request.method == 'POST':
        actions.task_title = request.POST.get('task_title', '')
        actions.save()

        return render(request, 'actions/actions.html', {'actions': actions})


    return render(request, 'actions/edit.html', {'actions': actions})
    
