from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def demo(request):
    # return HttpResponse('Hello ,World')
    person = {
        'name' : 'arafat islam',
        'age':20,
        'hobbies':['Music','cricket','sports','programming'],
        'gender': 'M'

    }

    location = "Dhaka"
    return render(request , 'index.html',{'loc': location , 'person':person})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def greet(request, person):
    display = request.GET.get('display','Default Value')
    page_number = request.GET.get('p',1)
    return render(request, 'person.html', {'person':person,'display':display, 'page_number':page_number})

def favnum(request, n):
    return HttpResponse('Your favorite number is: ' + str(n))