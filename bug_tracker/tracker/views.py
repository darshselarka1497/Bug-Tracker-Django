from django.shortcuts import render

from .models import Bug

# Create your views here.
def frontpage(request):
    bugs = Bug.objects.all()
    return render(request, 'tracker/frontpage.html', {'bugs': bugs})