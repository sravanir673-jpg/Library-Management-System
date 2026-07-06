from django.shortcuts import render
from .models import Book

def home(request):
    return render(request, 'home.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def issue(request):
    return render(request, 'issue.html')

def login(request):
    return render(request, 'login.html')

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {'book': book})