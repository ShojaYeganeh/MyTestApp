from django.shortcuts import render
from django.shortcuts import HttpResponse


def about(request):
    # return HttpResponse ('hi im here')
    return render(request,'about.html')

def Home(request):
    # return HttpResponse('Here my home what you say')
    return render(request,'home.html')
# def Nouyan(request):
    # return HttpResponse('He is my older son')
# def Farhan(request):
    # return HttpResponse('He is my younger son')
