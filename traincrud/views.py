from django.shortcuts import render,redirect
from .forms import Trainlog
from .models import Train

def train_list(request):
    context = {'train_list':Train.objects.all()}
    return render(request,"traincrud/train_list.html",  context)


def train_log(request):
    if request.method == "GET":
        log = Trainlog()
        return render(request,"traincrud/train_log.html", {'log':log})
    else:
        log = Trainlog(request.POST)
        if log.is_valid():
            log.save()
            return redirect('/list')

def train_delete(request):
    return 