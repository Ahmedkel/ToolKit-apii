from rest_framework import serializers
from .models import Website_Tools, Category
from django.contrib.auth.models import User


class Website_ToolsSerializer(serializers.ModelSerializer):
    """ This class is used to serialize the website_Tools model. """
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
        required=True
    )

    class Meta:
        model = Website_Tools
        fields = ['id', 'name', 'category', 'image', 'description', 'created_at', 'updated_at', 'pricing', 'url']
    
    def create(self, validated_data):
        """ Create a new website_tool object with the validated data."""
        category_name = validated_data.pop('category').name
        category, created = Category.objects.get_or_create(name=category_name)
        validated_data['category'] = category
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email']
