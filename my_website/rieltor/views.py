from .models import Flat
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import RieltorForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def all_flats(request):
    all_flat = Flat.objects.all()

    paginator = Paginator(all_flat, 10)
    page = request.GET.get('page')
    try:
        flats = paginator.page(page)
    except PageNotAnInteger:
        flats = paginator.page(1)
    except EmptyPage:
        flats = paginator.page(paginator.num_pages)

    context = {'flats': flats}
    template = 'rieltor/all_flats.html'

    return render(request, template, context)


def detail(request, flat_id):
    try:
        flat = Flat.objects.get(pk=flat_id)
    except Flat.DoesNotExist:
        raise Http404('Flat does not exist')
    return render(request, 'rieltor/detail.html', {'flat': flat})


@login_required
def add_new(request):
    form = RieltorForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        new_join.save()
        return redirect('all_flats')
    template = 'rieltor/add_new.html'
    context = {'form': form}
    return render(request, template, context)
