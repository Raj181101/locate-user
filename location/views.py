from django.shortcuts import render

# Create your views here.

def user_location(request):
    return render(request,'user_location.html')