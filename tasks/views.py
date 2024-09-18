from django.shortcuts import render

tasks = ["Read","Sing","Pray"]
 
# Create your views here.
def index(request):
    return render(request, "tasks/index.html",{
        "tasks": tasks
    })


# Add to task function
def add(request):
    return render(request, "tasks/add.html")