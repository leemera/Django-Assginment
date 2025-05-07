from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from todo.forms import TodoForm, TodoUpdateForm
from todo.models import Todo


@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by('created_at')
    q = request.GET.get('q')
    if q:
        todos = todos.filter(Q(title__icontains=q) | Q(description__icontains=q))
    paginator = Paginator(todos, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'todo/todo_list.html', {'page_obj': page_obj})


@login_required
def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'todo/todo_info.html', {'todo': todo.__dict__})


@login_required
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect(reverse('todo_info', kwargs={'todo_id': todo.pk}))
    return render(request, 'todo/todo_create.html', {'form': form})


@login_required
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    form = TodoUpdateForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect(reverse('todo_info', kwargs={'todo_id': todo.pk}))
    return render(request, 'todo/todo_update.html', {'form': form})


@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect(reverse('todo_list'))
