from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    course  = Course.objects.all()
    return render(request, 'index.html',{'course': course})