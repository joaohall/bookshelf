from typing import Any
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView

# Create your views here.



def home_page(request):
    books_list = Book.objects.select_related('rating').prefetch_related('rating_set__user').all()
    books_discount = Book.objects.filter(discount=True)
    books_trending = Book.objects.filter(trending=True)
    context = {
        'books': books_list,
        'books_discount':books_discount,
        'books_trending': books_trending
    }
            
    return render(request, 'home.html', context )

def cart_page(request):
    return render(request, 'cart.html')


def search_result(request):
    if request.method == "GET":
        search = request.GET.get('search')
        books_filtered = Book.objects.filter(title__contains=search) 
        return render(request, 'search.html', {'books_filtered': books_filtered})
    else: return render(request, 'search.html')
    
class book_detail(DetailView):
    template_name = 'book_detail.html'
    model = Book
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)