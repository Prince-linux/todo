from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import TodoItem
from todo.forms.todo_form import TodoForm


def index(request):
    item_form = TodoForm()
    return render(request, 'todo/index.html', {'form': item_form})

def save(request):
    item_form = TodoForm(request.POST)

    if item_form.is_valid():
        new_item = TodoItem()
        new_item.content = item_form.cleaned_data['content']
        new_item.author = item_form.cleaned_data['author']
        new_item.date_created = item_form.cleaned_data['date_created']
        new_item.completed = item_form.cleaned_data['completed']
        new_item.save()
        return HttpResponseRedirect('/list')
    else:
        return render(request, 'todo/index.html', {'form': item_form})

def lists(request):
    items = TodoItem.objects.all()
    return render(request, 'todo/lists.html', {'items':items})


def mark_as_done(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return HttpResponseRedirect('/list')


def mark_as_undone(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return HttpResponseRedirect('/list')

def delete(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    item.delete()
    return HttpResponseRedirect('/list')

def delete_all(self):
    TodoItem.objects.all().delete()
    return HttpResponseRedirect('/list')

def create_todo(self):
    return HttpResponseRedirect('/todo')


def create_new(self):
    return HttpResponseRedirect('/todo')





