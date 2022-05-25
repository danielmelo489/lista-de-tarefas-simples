from django.urls import reverse

from django.http import HttpResponseRedirect
from django.views import View

from django.views.generic import ListView

from .models import Task


class Home(ListView):
    model = Task
    context_object_name = 'list_tasks'


class Task_create(View):
    
    def post(self, request):
        new_task = Task()
        new_task.description = request.POST['task']
        new_task.save()

        return HttpResponseRedirect(reverse('core:home'))

class Task_delete(View):
    
    def post(self, request, id):
        task_deleted = Task.objects.filter(id=id)
        task_deleted.delete()
        return HttpResponseRedirect(reverse('core:home'))