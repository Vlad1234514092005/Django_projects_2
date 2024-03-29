from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book


def show_main_page(request):
    library = Book.objects.all()
    return render(request, 'books/mainpage.html', {'library': library})


def show_post_by_id(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/show_book_info.html', {'book': book})
