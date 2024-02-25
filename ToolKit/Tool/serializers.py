from rest_framework import serializers
from .models import website_Tools
from django.contrib.auth.models import User


class website_ToolsSerializer(serializers.ModelSerializer):
    """ This class is used to serialize the website_Tools model. """
    class Meta:
        model = website_Tools
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email']
