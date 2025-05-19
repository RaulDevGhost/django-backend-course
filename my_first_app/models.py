from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)

    def __str__(self):
        return f"{self.title} - {self.year}"

class Publisher(models.Model):
    name = models.TextField(max_length=250)
    address = models.TextField(max_length=250)
    city = models.TextField(max_length=250)
    state_province = models.TextField(max_length=250)
    country = models.TextField(max_length=250)
    website = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.name} - {self.city} - {self.country}"


class Author(models.Model):
    name = models.TextField(max_length=250)
    birth_date = models.DateField()
    email = models.TextField(max_length=250)
    bio = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Book(models.Model):
    title = models.TextField(max_length=250)
    authors = models.ManyToManyField(Author, related_name='authors')
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author} - {self.publication_date}"


