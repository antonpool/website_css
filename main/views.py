from django.shortcuts import render

from db.models import Table

def home (request):
    table = Table.objects.all()
    
    return render (request, 'main/home.html', {'table': table})


