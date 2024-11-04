from django.shortcuts import render

# Create your views here.
def django(request):
    return render(request, 'ex01/django.html')