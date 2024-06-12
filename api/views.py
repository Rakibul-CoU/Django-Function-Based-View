from django.shortcuts import render

from api.forms import BookForm
from api.models import Book
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)



# Create your views here.


def create_view(request):
    context = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'create_view.html', context)



def list_view(request):
    context = {}
    context['dataset'] = Book.objects.all()


    # You can perform here if other operations are required
    return render(request, 'list_view.html', context)


def detail_view(request, id):
    context = {}
    context['data'] = Book.objects.get(id=id)
    return render(request, 'detail_view.html', context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'update_view.html', context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Book, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/api/list-view/")
    return render(request, 'delete_view.html', context)
