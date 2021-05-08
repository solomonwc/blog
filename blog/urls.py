from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]
