from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.template.defaulttags import querystring

from .models import Book

def book_list(request):
    query = request.GET.get('q', '')
    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/book_list.html', {'page_obj':page_obj, 'query':query })
