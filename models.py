from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    description = models.TextField(default="")

class Issue(models.Model):
    student_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)