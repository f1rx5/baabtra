from django.shortcuts import render

# Create your views here.
def fnhome(request):
    return render(request,'home.html')
def fncourses(request):
    return render(request,'courses.html')
def fncontact(request):
    return render(request,'contact.html')