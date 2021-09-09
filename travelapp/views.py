from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import People

def travel(request):
    obj=Place.objects.all()
    obj1=People.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
