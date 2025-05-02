from django.shortcuts import render, redirect
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