from django.shortcuts import render

from library.Reader.models import Readers
from .models import Book 



# Create your views here.

def book_list(request):
    books = Book.objects.all()  
    return render(request, 'book_list.html', {'books': {'harry potter','lord of the Rings','sherlock'}})

def readers(request):
    reader_name = 'Tornike ozbetelashvili'  

    reader = Readers()
    if reader.fullName == reader_name:         
        books = reader.books.all()  

        return render(request, 'book_list.html', {'books': books})
    else:
        return render(request, 'error')