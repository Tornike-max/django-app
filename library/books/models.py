from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    max_pages = models.IntegerField(default=240)
    genre = models.CharField(max_length=100)  