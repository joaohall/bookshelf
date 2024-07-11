from django.shortcuts import render
from .models import Book


# Create your views here.



def home_page(request):
    books_list = Book.objects.all()
    books_discount = Book.objects.filter(discount=True)
    books_trending = Book.objects.filter(trending=True)
    context = {
        'books': books_list,
        'books_discount':books_discount,
        'books_treding': books_trending
    }
    return render(request, 'home.html', context )