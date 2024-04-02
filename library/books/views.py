from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .form import BookAddForm
from .models import Book


def show_main_page(request):
    library = Book.objects.all()
    return render(request, 'books/mainpage.html', {'library': library})


def show_post_by_id(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/show_book_info.html', {'book': book})


def add_book(request):
    if request.method == "POST":
        form = BookAddForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('show_main_page')
    else:
        form = BookAddForm
    return render(request, 'books/add_book.html', {'form': form})


def update_book(request, pk):
    post = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookAddForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('show_main_page')
    else:
        form = BookAddForm(instance=post)
    return render(request, 'books/add_book.html', {'form': form})


def delete_book(request):
    return HttpResponse("<h1>Deleting article</h1>")
