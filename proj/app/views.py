from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def dubai(request):
    return render(request,'dubai.html')

def india(request):
    return render(request,'india.html')

def australia(request):
    return render(request,'australia.html')

def america(request):
    return render(request,'america.html')