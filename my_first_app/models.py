from django.db import models
from .managers import PublisherManager, AuthorManager, ProfileManager, BookManager


class Publisher(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state_province = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    website = models.CharField(max_length=250)

    # Assign the custom manager
    objects = PublisherManager()

    def __str__(self):
        return f"{self.name} - {self.city} - {self.country}"


class Author(models.Model):
    name = models.CharField(max_length=250)
    birth_date = models.DateField()
    email = models.CharField(max_length=250)
    bio = models.TextField(max_length=1000)

    # Assign the custom manager
    objects = AuthorManager()

    def __str__(self):
        return f"{self.name} - {self.email}"


class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.SET_DEFAULT, default=None, null=True)
    user = models.CharField(max_length=250)
    bio = models.TextField(max_length=1000) 
    website = models.URLField(max_length=250)

    # Assign the custom manager
    objects = ProfileManager()

    def __str__(self):
        return f"{self.user} - {self.website}"


class Book(models.Model):
    title = models.CharField(max_length=250)
    # Changed related_name to avoid conflicts
    authors = models.ManyToManyField(Author, related_name='books')
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    # Assign the custom manager
    objects = BookManager()

    def __str__(self):
        # Fixed to handle multiple authors
        author_names = ", ".join([author.name for author in self.authors.all()])
        return f"{self.title} - {author_names} - {self.publication_date}"