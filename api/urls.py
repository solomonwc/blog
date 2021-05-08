from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ArticleViewSet


route = routers.DefaultRouter()
route.register('user', UserViewSet, basename='user')
route.register('article', ArticleViewSet, basename='article')


app_name = 'api'
urlpatterns = [
    path('', include(route.urls))
]