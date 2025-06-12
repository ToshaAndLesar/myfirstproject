from django.shortcuts import render


def index(request):
    x = 2**100
    return render(request, 'myFirstProject/index.html', {"x":x})