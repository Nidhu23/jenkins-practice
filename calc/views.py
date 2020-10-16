from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'nidhuna'})


def add(request):
    value_one = int(request.POST['num1'])
    value_two = int(request.POST['num2'])
    result = value_one+value_two
    return render(request, 'result.html', {'result': result})
