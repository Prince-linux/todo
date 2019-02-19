from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
	all_todo_items = TodoItem.objects.all()
	return render(request, 'index.html', {'all_items': all_todo_items})

def addTodo(request):
	new_item = TodoItem(content = request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('/todo/')
