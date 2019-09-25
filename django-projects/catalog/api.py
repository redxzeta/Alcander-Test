from catalog.models import Author
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer, UserSerializer
from django.contrib.auth.models import User
# catalog viewset


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AuthorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
