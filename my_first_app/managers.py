from django.db import models
from django.db.models import Count, Q
from datetime import datetime, timedelta

# Manager for the Publisher model
class PublisherManager(models.Manager):
    # noinspection PyUnresolvedReferences
    def get_by_country(self, country):
        """Get publishers from a specific country"""
        return self.filter(country__iexact=country)

    # noinspection PyUnresolvedReferences
    def search(self, query):
        """Search publishers by name or city"""
        return self.filter(
            Q(name__icontains=query) |
            Q(city__icontains=query)
        )

    # noinspection PyUnresolvedReferences
    def with_book_count(self):
        """Return publishers with their published book count"""
        # The 'book' here refers to the lowercase name of the Book model
        # that has a ForeignKey to Publisher
        return self.annotate(book_count=Count('book'))


# Manager for the Author model
class AuthorManager(models.Manager):
    # noinspection PyUnresolvedReferences
    def get_by_birth_year(self, year):
        """Get authors born in a specific year"""
        return self.filter(birth_date__year=year)

    # noinspection PyUnresolvedReferences
    def search(self, query):
        """Search authors by name or email"""
        return self.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query)
        )

    # noinspection PyUnresolvedReferences
    def with_book_count(self):
        """Return authors with the count of books they've written"""
        # 'books' is the related_name specified in the Book model's ManyToManyField
        return self.annotate(book_count=Count('books'))

    # noinspection PyUnresolvedReferences
    def prolific_authors(self, min_books=3):
        """Get authors with more than X books"""
        return self.annotate(book_count=Count('books')).filter(book_count__gte=min_books)


# Manager for the Profile model
class ProfileManager(models.Manager):
    # noinspection PyUnresolvedReferences
    def with_author(self):
        """Get profiles with author information"""
        return self.select_related('author')

    # noinspection PyUnresolvedReferences
    def without_author(self):
        """Get profiles without an associated author"""
        return self.filter(author__isnull=True)


# Manager for the Book model
class BookManager(models.Manager):
    # noinspection PyUnresolvedReferences
    def get_by_year(self, year):
        """Get books published in a specific year"""
        return self.filter(publication_date__year=year)

    # noinspection PyUnresolvedReferences
    def recent_books(self, years=5):
        """Get books published in the last X years"""
        cutoff_date = datetime.now() - timedelta(days=365 * years)
        return self.filter(publication_date__gte=cutoff_date)

    # noinspection PyUnresolvedReferences
    def search(self, query):
        """Search books by title"""
        return self.filter(title__icontains=query)

    # noinspection PyUnresolvedReferences
    def by_publisher(self, publisher_name):
        """Find books from a specific publisher"""
        return self.filter(publisher__name__icontains=publisher_name)

    # noinspection PyUnresolvedReferences
    def by_author(self, author_name):
        """Find books by a specific author"""
        return self.filter(authors__name__icontains=author_name)

    # noinspection PyUnresolvedReferences
    def with_author_count(self):
        """Return books with their author count"""
        return self.annotate(author_count=Count('authors'))

    # noinspection PyUnresolvedReferences
    def multi_author_books(self):
        """Get books with more than one author"""
        return self.annotate(author_count=Count('authors')).filter(author_count__gt=1)