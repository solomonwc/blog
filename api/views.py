from rest_framework import viewsets
from .models import UserInfo, Article
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, ArticleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=True)
    def contents(self, request, *args, **kwargs):
        return Response("Hello World")


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer