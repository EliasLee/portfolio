from django.shortcuts import render
from gallery.models import Gallery


def home(request):
    get = Gallery.objects
    return render(request,'home.html',{'jess':get})
