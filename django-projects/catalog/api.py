from catalog.models import Author
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer

# catalog viewset


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AuthorSerializer
