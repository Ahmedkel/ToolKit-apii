from rest_framework import serializers
from .models import website_Tools
from django.contrib.auth.models import User


class website_ToolsSerializer(serializers.ModelSerializer):
    """ This class is used to serialize the website_Tools model. """
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = website_Tools
        fields = ['id', 'name', 'category_name','description', 'created_at', 'updated_at', 'pricing', 'url']

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email']
