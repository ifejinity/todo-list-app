from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
import uuid
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'to_do_list/index.html', {
        'message': 'This is your first template!',
        'todos': todos
    })

def create_todo(request):
    task = request.POST.get('task')
    Todo.objects.create(
        id=uuid.uuid4(),
        task=task,
        completed=False
    )
    return redirect('index')

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('index')

def update_todo(request, id):
    task = request.POST.get('task')
    completed = request.POST.get('completed') == 'on'
    todo = get_object_or_404(Todo, id=id)
    todo.task = task
    todo.completed = completed
    todo.save()
    return redirect('index')