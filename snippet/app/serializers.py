from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Snippet, Tag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields ='__all__'

class SnippetSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = Snippet
        fields ='__all__'


