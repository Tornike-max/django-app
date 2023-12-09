from django.shortcuts import render
from .models import Readers

def reader(request):
    readers = Readers.objects.all() 
    return render(request, 'reader.html', {'readers': {'fullName':'Tornike ozbetelashvili','email':'tornike@gmail.com'}})