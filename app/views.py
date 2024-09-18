from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
   return render(request, "hello/index.html")


def hope(request):
    return HttpResponse('Hi thre mr Hope')

# def greet(request, name):
#     return HttpResponse(f"Hi {name.capitalize()}");



def greet(request, name):
        return render(request, "hello/greet.html" ,{
             "name": name.capitalize()
        })

  