from rest_framework import serializers
from .models import UserInfo, Article


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'password', 'email', 'token']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'