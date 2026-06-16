from rest_framework import permissions, viewsets
from django.contrib.auth import get_user_model
from .serializers import AuthorSerializer, BookSerializer, UserSerializer
from books.models import Author, Book

UserModel = get_user_model()

class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny,]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny,]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny,]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()