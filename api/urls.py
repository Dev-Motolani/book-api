from django.urls import path
from rest_framework import routers 
from .views import AuthorViewSet, BookViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')

urlpatterns = router.urls
