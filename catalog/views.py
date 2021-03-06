from django.shortcuts import render
from catalog.models import Book, BookInstance, Author, Genre

# Create your views here.
def index(request):
  # View function for home page of site

  # Generate counts of some of the main objects
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()

  # Available Books (status = 'a')
  num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

  # All() is implied by defailt
  num_authors = Author.objects.count()

  num_genres = Genre.objects.count()

  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available' : num_instances_available,
    'num_authors' : num_authors,
    'num_genres' : num_genres,
  }

  # Render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
  model = Book
  # context_object_name = 'my_book_list'
  # queryset = Book.objects.filter(author__icontains='king') # filters all books who have the author name of king somehwere
  # template_name = 'books/my_arbitrary_template_name_list.html'