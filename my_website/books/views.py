from django.shortcuts import render

from .models import Author
from django.shortcuts import render
from django.http import Http404

def index(request):
    all_authors = Author.objects.all()

    return render(request, 'books/index.html',{'all_authors':all_authors})

def detail(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        raise Http404('Author does not exist')
    return render(request,'books/detail.html',{'author':author})

