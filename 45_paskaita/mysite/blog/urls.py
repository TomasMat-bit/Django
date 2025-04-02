from django.urls import path
from . import views
from .views import PostListViews, PostDeleteView, PostCreateView, PostUpdateView, PostDetailView

urlpatterns = [
    path('', PostListViews.as_view(), name='post_list'),
    path('<int:pk>/', PostDeleteView.as_view(), name='post_detail'),
    path('naujas/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/redaguoti/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/istrinti/',PostDetailView.as_view(), name='post_delete'),
]