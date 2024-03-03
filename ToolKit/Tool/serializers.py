from rest_framework import serializers
from .models import website_Tools, Category
from django.contrib.auth.models import User


class website_ToolsSerializer(serializers.ModelSerializer):
    """ This class is used to serialize the website_Tools model. """
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = website_Tools
        fields = ['id', 'name', 'category_name','description', 'created_at', 'updated_at', 'pricing', 'url']
        
    def create(self, validated_data):
        """ Create a new website_tool object with the validated data."""
        category_name = validated_data.pop('category')['name']
        category, created = Category.objects.get_or_create(name=category_name)
        website_tool = website_Tools.objects.create(category=category, **validated_data)
        return website_tool
    
    def validate_category(self, value):
        """ Custom validation for the category field. """
        # Example: Check if the category name is valid
        if not Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Invalid category name.")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email']
