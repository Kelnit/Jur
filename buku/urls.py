from django.urls import path
from buku.views import AuthorCollection, BookCollection

urlpatterns = [
  path('authors/', AuthorCollection.as_view()),
  path('books/', BookCollection.as_view()),
]
