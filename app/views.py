from django.shortcuts import render,redirect
from .models import Work

def index(request):
    context = {

    }
    return render(request, 'dist/index.html')

def reach(request):
    context = {

    }
    return render(request, 'dist/contact.html')

def about(request):
    context = {

    }
    return render(request, 'dist/about.html')
def work(request):
    queryset = Work.objects.all()
    context = {
        'queryset' :queryset
    }
    return render(request, 'dist/work.html', context)