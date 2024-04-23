from rest_framework import serializers
from .models import Website_Tools, Category
from django.contrib.auth.models import User


class Website_ToolsSerializer(serializers.ModelSerializer):
    """ This class is used to serialize the website_Tools model. """
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=True
    )

    class Meta:
        model = Website_Tools
        fields = ['id', 'name', 'category', 'image', 'description', 'created_at', 'updated_at', 'pricing', 'url']

