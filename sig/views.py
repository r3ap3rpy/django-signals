from django.shortcuts import render
from .models import Topics
# Create your views here.
def index(request):
    topics = Topics.objects.all()
    return render(request,'sig/index.html',{'topics':topics})