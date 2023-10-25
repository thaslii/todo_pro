from django.shortcuts import render,redirect
from .models import Task
from .forms import TodoForm

# Create your views here.

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy

class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvindex')









def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,'index.html',{'task1':task1})

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})
    