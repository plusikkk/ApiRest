from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='books')
    genre = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    popularity = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name
