from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from rieltor.models import Flat
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_el_pagination.el_pagination.decorators import page_template

@page_template('home/entry_home_page.html')
def home_page(request, template = 'home/home_page.html', extra_context=None):

    '''paginator = Paginator(all_flat, 5)
    page = request.GET.get('page')
    try:
        flats = paginator.page(page)
    except PageNotAnInteger:
        flats = paginator.page(1)
    except EmptyPage:
        flats = paginator.page(paginator.num_pages)'''

    context = {'flats': Flat.objects.all(),
               }
    if extra_context is not None:
        context.update(extra_context)
    return render(request,template, context)
