from django.shortcuts import render,redirect

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
    context = {

    }
    return render(request, 'dist/work.html')