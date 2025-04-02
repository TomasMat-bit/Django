from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('prideti/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
