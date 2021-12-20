from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return f'{self.title}'


class CommentBook(models.Model):
    post = models.ForeignKey(Book, on_delete=models.CASCADE,
                                related_name='book_comment')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)