from django.shortcuts import render

def train_list(request):
    
    return render(request,"traincrud/train_list.html")


def train_log(request):
    return render(request,"traincrud/train_log.html")


def train_delete(request):
    return 