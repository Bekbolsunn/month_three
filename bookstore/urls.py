from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books, name='book_view'),
    path('books/<int:id>/', views.book_detail, name='book_detail_view'),
    path('add-book/', views.add_book, name='add_post_view'),
    path('add-comment-book/', views.add_comment_book, name='add_comment_book_view'),
]