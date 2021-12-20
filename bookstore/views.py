from django import forms
from django.http import request
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from . import models, forms

# Create your views here.
def get_books(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})

def book_detail(request, id):
    try:
        book = models.Book.objects.get(id=id)
        try:
            comment = models.CommentBook.objects.filter(post_id=id).order_by('created_date')
        except models.CommentBook.DoesNotExist:
            return HttpResponse('No Comments')

    except models.Book.DoesNotExist:
        raise Http404('Book does not exist, badboy')

    return render(request, 'book_detail.html', {'book':book, 'book_comment': comment})





def add_book(request):
    method = request.method
    if method == "BOOK":
        form = forms.BookForm(request.BOOK, request.FILES)
        print(form.data)
        models.Book.objects.create(title=form.data['title'],
                                    description = form.data['description'],
                                    image=form.data['image'])
        return HttpResponse('Book Added Successfully')
    else:
        form = forms.BookForm()

    return render(request, 'book_add.html', {'form': form})


def add_comment_book(request):
    method = request.method
    if method == 'BOOK':
        form = forms.CommentBookForm(request.BOOK, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponse('Comment Created Succssefully')
    else:
        form = forms.CommentBookForm()
    return render(request, 'book_comment.html', {'form': form})