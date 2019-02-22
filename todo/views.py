from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from todo.forms.todo_form import TodoForm

def index(request):
    item_form = TodoForm()
    #items = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'form': item_form}) #'items':items})

def save(request):
    item_form = TodoForm(request.POST)

    if item_form.is_valid():
        new_item = TodoItem()
        new_item.content = item_form.cleaned_data['content']
        new_item.author = item_form.cleaned_data['author']
        new_item.date_created = item_form.cleaned_data['date_created']
        new_item.completed = item_form.cleaned_data['completed']
        new_item.save()
        return HttpResponseRedirect('/todo')
    else:
        return render(request, 'todo/index.html', {'form': item_form})

def lists(request):
    items = TodoItem.objects.all()
    return render(request, 'todo/lists.html', {'items':items})

