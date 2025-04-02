from rest_framework import viewsets
from .models import Book
from .serialiser import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSetByID(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        obj = super().get_object()
        return obj

# Create your views here.
