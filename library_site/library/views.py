from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html", {"books": books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "library/book_detail.html", {"book": book})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("library:book_detail", pk=book.pk)
    else:
        form = BookForm()
    return render(request, "library/book_form.html",
                  {"form": form, "title": "Добавить книгу"})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("library:book_detail", pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, "library/book_form.html",
                  {"form": form, "title": "Изменить книгу", "book": book})
