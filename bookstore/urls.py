from django.urls import path

from bookstore.views import BooksList, BookDetail, AuthorsList, AuthorDetail, PublishersList, PublisherDetail

urlpatterns = [
    path('books', BooksList.as_view()),
    path('books/<int:pk>', BookDetail.as_view()),
    path('authors', AuthorsList.as_view()),
    path('authors/<int:pk>', AuthorDetail.as_view()),
    path('publishers', PublishersList.as_view()),
    path('publishers/<int:pk>', PublisherDetail.as_view())
]
