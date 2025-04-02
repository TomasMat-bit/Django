from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# Knygų sąrašas
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

# Vienos knygos peržiūra
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

# Naujos knygos kūrimas
class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author']
    success_url = reverse_lazy('book_list')  # Po sėkmingo įrašo grįžti į knygų sąrašą

# Knygos pašalinimas
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book_list')  # Po sėkmingo pašalinimo grįžti į knygų sąrašą
