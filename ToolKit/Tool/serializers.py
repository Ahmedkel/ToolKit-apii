from rest_framework import serializers
from .models import website_Tools


class website_ToolsSerializer(serializers.ModelSerializer):
    """ This class is used to serialize the website_Tools model. """
    class Meta:
        model = website_Tools
        fields = '__all__'