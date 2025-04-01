from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q

def post_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
    else:
        posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'page_list.html',
                  {
                         'page_obj': page_obj,
                         'query': query
                         }
        )
# pvz kaip supostinti 200 irasu su SHELL

# def super_loop():
#     from app.models import Post
#
#     for i in range(1, 201):
#         Post.objects.create(
#             title=f'Postas Nr. {i}',
#             body=f'Tai yra posto body Nr. {i}'
#         )

