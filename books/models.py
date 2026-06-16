from django.db import models


# Create your models here.
class Author(models.Model):
    # model an author
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    # model a book
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
       related_name='books', blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
