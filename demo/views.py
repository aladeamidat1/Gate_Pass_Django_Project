from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Gatepass Application")

def about(request):
    return render(request,"about.html")
