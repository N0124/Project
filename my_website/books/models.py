from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=250)
    years = models.CharField(max_length=500)
    country = models.CharField(max_length=250)
    photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name+', '+ self.country


class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    book_title = models.CharField(max_length=1000)
    year_of_publishing = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)

    def __str__(self):
        return self.book_title


